# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 971feb9
- commit date: 2024-10-01
- overall geometric mean: 1.448x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                        |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                       |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 405 ms: 2.15x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 892 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.78x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.8 ms: 1.85x faster                                                       |
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                       |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 76.7 ms: 1.30x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                       |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                       |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                       |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                       |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                       |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.53x faster                                                       |
| richards_super           | 94.7 ms                                                | 38.5 ms: 2.46x faster                                                       |
| richards                 | 79.3 ms                                                | 32.7 ms: 2.42x faster                                                       |
| generators               | 80.1 ms                                                | 34.1 ms: 2.35x faster                                                       |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 26.8 us: 2.18x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 405 ms: 2.15x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 892 ms: 1.98x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 64.9 ms: 1.97x faster                                                       |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.91x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 62.2 ms: 1.90x faster                                                       |
| go                       | 240 ms                                                 | 127 ms: 1.88x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                        |
| nbody                    | 154 ms                                                 | 82.8 ms: 1.85x faster                                                       |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                        |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                        |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.78x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                      |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                       |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                        |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                                       |
| pyflate                  | 716 ms                                                 | 441 ms: 1.62x faster                                                        |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                       |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                        |
| pylint                   | 551 ms                                                 | 364 ms: 1.51x faster                                                        |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 691 ms: 1.47x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.40 ms: 1.47x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                      |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                                        |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                      |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                      |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                       |
| thrift                   | 1.07 ms                                                | 791 us: 1.36x faster                                                        |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                        |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 76.7 ms: 1.30x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                        |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                                       |
| nqueens                  | 106 ms                                                 | 89.6 ms: 1.18x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                       |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                       |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                       |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                        |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                      |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                       |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                       |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| pickle_list              | 5.08 us                                                | 5.06 us: 1.00x faster                                                       |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                       |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                        |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                                       |
| coverage                 | 79.4 ms                                                | 85.9 ms: 1.08x slower                                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                       |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                       |
| unpack_sequence          | 60.0 ns                                                | 105 ns: 1.75x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, unpickle_list
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_optimize
Ignored benchmarks (5) of results/bm-20241001-3.14.0a0-971feb9-JIT/bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.448x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.19x