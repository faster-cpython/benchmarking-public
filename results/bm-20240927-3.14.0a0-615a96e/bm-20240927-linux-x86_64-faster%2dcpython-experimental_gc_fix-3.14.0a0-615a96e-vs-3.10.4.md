# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 615a96e
- commit date: 2024-09-27
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.31x faster                                                           |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                         |
| html5lib       | 88.9 ms                                                | 67.9 ms: 1.31x faster                                                          |
| tornado_http   | 136 ms                                                 | 91.0 ms: 1.50x faster                                                          |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 654 ms: 2.70x faster                                                           |
| async_tree_none         | 728 ms                                                 | 301 ms: 2.42x faster                                                           |
| async_tree_memoization  | 870 ms                                                 | 370 ms: 2.35x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 536 ms: 1.90x faster                                                           |
| Geometric mean          | (ref)                                                  | 2.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.2 ms: 1.74x faster                                                          |
| float          | 117 ms                                                 | 92.7 ms: 1.26x faster                                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                           |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                          |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                           |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 61.5 ms: 1.29x faster                                                          |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 88.1 ms: 1.13x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                           |
| unpickle_list        | 5.20 us                                                | 5.14 us: 1.01x faster                                                          |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                                          |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 129 ms: 1.11x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                          |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                          |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                          |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                          |
| genshi_xml      | 66.0 ms                                                | 52.2 ms: 1.26x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                                           |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 654 ms: 2.70x faster                                                           |
| async_tree_none          | 728 ms                                                 | 301 ms: 2.42x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.39x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 370 ms: 2.35x faster                                                           |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                           |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                           |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 478 ms: 1.93x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                          |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 536 ms: 1.90x faster                                                           |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                           |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                           |
| richards_super           | 94.7 ms                                                | 52.4 ms: 1.81x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.78x faster                                                          |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                           |
| nbody                    | 154 ms                                                 | 88.2 ms: 1.74x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                          |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                           |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                           |
| pyflate                  | 716 ms                                                 | 463 ms: 1.55x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                         |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                           |
| tornado_http             | 136 ms                                                 | 91.0 ms: 1.50x faster                                                          |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                          |
| logging_format           | 9.09 us                                                | 6.29 us: 1.45x faster                                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                         |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.42x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                           |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                          |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                          |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                           |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.33x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                          |
| nqueens                  | 106 ms                                                 | 80.1 ms: 1.32x faster                                                          |
| html5lib                 | 88.9 ms                                                | 67.9 ms: 1.31x faster                                                          |
| 2to3                     | 348 ms                                                 | 267 ms: 1.31x faster                                                           |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                                          |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 61.5 ms: 1.29x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 52.2 ms: 1.26x faster                                                          |
| float                    | 117 ms                                                 | 92.7 ms: 1.26x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 797 us: 1.24x faster                                                           |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                           |
| unpack_sequence          | 60.0 ns                                                | 51.7 ns: 1.16x faster                                                          |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                          |
| json                     | 5.69 ms                                                | 4.93 ms: 1.15x faster                                                          |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.14x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 88.1 ms: 1.13x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                           |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                           |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                           |
| unpickle_list            | 5.20 us                                                | 5.14 us: 1.01x faster                                                          |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                                          |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                                          |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                                          |
| gc_traversal             | 3.62 ms                                                | 3.89 ms: 1.07x slower                                                          |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 129 ms: 1.11x slower                                                           |
| telco                    | 7.27 ms                                                | 8.39 ms: 1.15x slower                                                          |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                   |

Benchmark hidden because not significant (4): asyncio_websockets, pickle_list, bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240927-3.14.0a0-615a96e/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.425x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.11x