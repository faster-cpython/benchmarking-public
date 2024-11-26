# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: 506492e
- commit date: 2024-09-20
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                          |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                           |
| tornado_http   | 136 ms                                                 | 91.1 ms: 1.50x faster                                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 312 ms: 2.33x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 390 ms: 2.23x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 850 ms: 2.08x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 557 ms: 1.83x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.7 ms: 1.75x faster                                                           |
| float          | 117 ms                                                 | 76.2 ms: 1.54x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.53x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.07x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                           |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.40 us: 1.04x slower                                                           |
| pickle               | 10.7 us                                                | 11.2 us: 1.05x slower                                                           |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                           |
| django_template | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                                            |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                           |
| async_tree_none          | 728 ms                                                 | 312 ms: 2.33x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 390 ms: 2.23x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 850 ms: 2.08x faster                                                            |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                            |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                           |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 481 ms: 1.92x faster                                                            |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                            |
| logging_silent           | 190 ns                                                 | 103 ns: 1.83x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 557 ms: 1.83x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.77x faster                                                           |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.76x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                           |
| nbody                    | 154 ms                                                 | 87.7 ms: 1.75x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                           |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.67x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                           |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                            |
| float                    | 117 ms                                                 | 76.2 ms: 1.54x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.53x faster                                                          |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                           |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                            |
| tornado_http             | 136 ms                                                 | 91.1 ms: 1.50x faster                                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                           |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                           |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| unpack_sequence          | 60.0 ns                                                | 42.2 ns: 1.42x faster                                                           |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                           |
| django_template          | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                           |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                           |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.33x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                           |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.27x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 792 us: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                          |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                           |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                           |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.07x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                            |
| async_generators         | 444 ms                                                 | 433 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.13 us: 1.01x slower                                                           |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.40 us: 1.04x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.79 ms: 1.05x slower                                                           |
| pickle                   | 10.7 us                                                | 11.2 us: 1.05x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                           |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                                           |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                                           |
| telco                    | 7.27 ms                                                | 8.32 ms: 1.15x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-506492e/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.436x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x