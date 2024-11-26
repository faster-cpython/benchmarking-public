# Results vs. 3.12.0

- fork: efimov-mikhail
- ref: crash_fix_generators
- machine: linux-x86_64
- commit hash: b94d5c4
- commit date: 2024-10-15
- overall geometric mean: 1.054x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.6 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.0 ms: 1.09x faster                                                           |
| nbody          | 97.0 ms                                                | 89.4 ms: 1.08x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.04x faster                                                           |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                            |
| unpickle_list        | 5.29 us                                                | 5.16 us: 1.03x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.03x faster                                                            |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.02x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 371 us                                                 | 264 us: 1.41x faster                                                            |
| unpack_sequence          | 54.0 ns                                                | 40.0 ns: 1.35x faster                                                           |
| deepcopy_memo            | 40.7 us                                                | 31.2 us: 1.31x faster                                                           |
| comprehensions           | 21.8 us                                                | 16.7 us: 1.30x faster                                                           |
| deepcopy_reduce          | 3.35 us                                                | 2.70 us: 1.24x faster                                                           |
| pathlib                  | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                           |
| go                       | 139 ms                                                 | 120 ms: 1.17x faster                                                            |
| raytrace                 | 312 ms                                                 | 268 ms: 1.17x faster                                                            |
| logging_simple           | 6.46 us                                                | 5.55 us: 1.16x faster                                                           |
| logging_format           | 7.23 us                                                | 6.25 us: 1.16x faster                                                           |
| regex_compile            | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| sympy_sum                | 169 ms                                                 | 148 ms: 1.15x faster                                                            |
| deltablue                | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                           |
| tornado_http             | 103 ms                                                 | 90.6 ms: 1.13x faster                                                           |
| generators               | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                           |
| crypto_pyaes             | 81.9 ms                                                | 73.2 ms: 1.12x faster                                                           |
| sympy_str                | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| tomli_loads              | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| scimark_monte_carlo      | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                           |
| chaos                    | 67.0 ms                                                | 60.9 ms: 1.10x faster                                                           |
| float                    | 84.7 ms                                                | 78.0 ms: 1.09x faster                                                           |
| nbody                    | 97.0 ms                                                | 89.4 ms: 1.08x faster                                                           |
| 2to3                     | 274 ms                                                 | 253 ms: 1.08x faster                                                            |
| unpickle                 | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| sympy_integrate          | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                           |
| pprint_safe_repr         | 776 ms                                                 | 720 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                           |
| meteor_contest           | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| json_loads               | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| scimark_fft              | 382 ms                                                 | 360 ms: 1.06x faster                                                            |
| unpickle_pure_python     | 230 us                                                 | 217 us: 1.06x faster                                                            |
| dulwich_log              | 68.5 ms                                                | 64.7 ms: 1.06x faster                                                           |
| pprint_pformat           | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| docutils                 | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                          |
| pyflate                  | 482 ms                                                 | 457 ms: 1.06x faster                                                            |
| mako                     | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| mdp                      | 2.63 sec                                               | 2.49 sec: 1.05x faster                                                          |
| sqlglot_transpile        | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                           |
| async_generators         | 463 ms                                                 | 440 ms: 1.05x faster                                                            |
| pickle_pure_python       | 324 us                                                 | 308 us: 1.05x faster                                                            |
| sqlglot_parse            | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                           |
| sqlglot_normalize        | 110 ms                                                 | 105 ms: 1.05x faster                                                            |
| sympy_expand             | 478 ms                                                 | 458 ms: 1.04x faster                                                            |
| xml_etree_generate       | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| xml_etree_process        | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                           |
| fannkuch                 | 417 ms                                                 | 401 ms: 1.04x faster                                                            |
| regex_effbot             | 3.61 ms                                                | 3.49 ms: 1.04x faster                                                           |
| nqueens                  | 83.3 ms                                                | 80.5 ms: 1.04x faster                                                           |
| sqlglot_optimize         | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                           |
| xml_etree_iterparse      | 107 ms                                                 | 104 ms: 1.03x faster                                                            |
| scimark_lu               | 118 ms                                                 | 115 ms: 1.03x faster                                                            |
| json                     | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                           |
| unpickle_list            | 5.29 us                                                | 5.16 us: 1.03x faster                                                           |
| xml_etree_parse          | 159 ms                                                 | 156 ms: 1.03x faster                                                            |
| django_template          | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                           |
| asyncio_tcp              | 491 ms                                                 | 480 ms: 1.02x faster                                                            |
| scimark_sor              | 129 ms                                                 | 127 ms: 1.02x faster                                                            |
| hexiom                   | 6.41 ms                                                | 6.31 ms: 1.02x faster                                                           |
| pickle_dict              | 35.5 us                                                | 35.0 us: 1.02x faster                                                           |
| pycparser                | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                          |
| bench_thread_pool        | 842 us                                                 | 837 us: 1.01x faster                                                            |
| logging_silent           | 104 ns                                                 | 104 ns: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| pidigits                 | 187 ms                                                 | 187 ms: 1.00x slower                                                            |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| richards_super           | 51.5 ms                                                | 52.1 ms: 1.01x slower                                                           |
| sqlite_synth             | 2.83 us                                                | 2.87 us: 1.01x slower                                                           |
| python_startup_no_site   | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 158 us                                                 | 161 us: 1.02x slower                                                            |
| spectral_norm            | 115 ms                                                 | 117 ms: 1.02x slower                                                            |
| pickle                   | 11.6 us                                                | 11.9 us: 1.03x slower                                                           |
| coroutines               | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                           |
| regex_v8                 | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                           |
| gc_traversal             | 3.79 ms                                                | 4.02 ms: 1.06x slower                                                           |
| json_dumps               | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| python_startup           | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                    | 7.10 ms                                                | 7.98 ms: 1.12x slower                                                           |
| coverage                 | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                           |
| create_gc_cycles         | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (3): regex_dna, richards, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a0-b94d5c4/bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.054x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x