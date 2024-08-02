# Results vs. 3.13.0b2

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.03x slower
- HPT reliability: 88.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 269 ms: 1.02x faster                                                  |
| chameleon      | 7.22 ms                                                    | 7.08 ms: 1.02x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.81 sec: 1.01x faster                                                |
| html5lib       | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 93.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|--------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 363 ms: 1.04x faster                                                  |
| async_tree_none_tg | 336 ms                                                     | 349 ms: 1.04x slower                                                  |
| async_tree_io_tg   | 936 ms                                                     | 981 ms: 1.05x slower                                                  |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                  |
| nbody          | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                  |
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 61.5 ms: 1.01x slower                                                 |
| pickle_dict          | 34.8 us                                                    | 35.1 us: 1.01x slower                                                 |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                  |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 89.0 ms: 1.02x slower                                                 |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.29 us: 1.04x slower                                                 |
| unpickle             | 15.1 us                                                    | 16.1 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (5): unpickle_list, xml_etree_iterparse, json_dumps, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                      | 2.79 sec                                                   | 2.57 sec: 1.09x faster                                                |
| gc_traversal             | 3.98 ms                                                    | 3.67 ms: 1.08x faster                                                 |
| richards                 | 50.9 ms                                                    | 48.0 ms: 1.06x faster                                                 |
| richards_super           | 57.4 ms                                                    | 54.5 ms: 1.05x faster                                                 |
| async_tree_none          | 378 ms                                                     | 363 ms: 1.04x faster                                                  |
| crypto_pyaes             | 77.5 ms                                                    | 74.5 ms: 1.04x faster                                                 |
| python_startup           | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| scimark_lu               | 122 ms                                                     | 117 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.10 ms: 1.03x faster                                                 |
| scimark_fft              | 392 ms                                                     | 382 ms: 1.03x faster                                                  |
| regex_dna                | 221 ms                                                     | 215 ms: 1.03x faster                                                  |
| deepcopy_reduce          | 3.35 us                                                    | 3.27 us: 1.02x faster                                                 |
| pyflate                  | 484 ms                                                     | 474 ms: 1.02x faster                                                  |
| dulwich_log              | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                 |
| chameleon                | 7.22 ms                                                    | 7.08 ms: 1.02x faster                                                 |
| scimark_monte_carlo      | 69.2 ms                                                    | 67.9 ms: 1.02x faster                                                 |
| 2to3                     | 274 ms                                                     | 269 ms: 1.02x faster                                                  |
| chaos                    | 61.3 ms                                                    | 60.3 ms: 1.02x faster                                                 |
| sqlite_synth             | 2.99 us                                                    | 2.94 us: 1.02x faster                                                 |
| coroutines               | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                 |
| nqueens                  | 81.4 ms                                                    | 80.3 ms: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                  |
| generators               | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                |
| regex_compile            | 137 ms                                                     | 135 ms: 1.01x faster                                                  |
| sympy_str                | 282 ms                                                     | 279 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                 |
| mako                     | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| spectral_norm            | 116 ms                                                     | 115 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 110 ms                                                     | 109 ms: 1.01x faster                                                  |
| tornado_http             | 94.6 ms                                                    | 93.9 ms: 1.01x faster                                                 |
| docutils                 | 2.83 sec                                                   | 2.81 sec: 1.01x faster                                                |
| sqlglot_transpile        | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.42 us: 1.01x faster                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                 |
| sympy_expand             | 473 ms                                                     | 469 ms: 1.01x faster                                                  |
| asyncio_websockets       | 567 ms                                                     | 563 ms: 1.01x faster                                                  |
| go                       | 145 ms                                                     | 144 ms: 1.01x faster                                                  |
| sqlglot_optimize         | 55.5 ms                                                    | 55.2 ms: 1.01x faster                                                 |
| logging_silent           | 105 ns                                                     | 104 ns: 1.00x faster                                                  |
| deepcopy                 | 367 us                                                     | 366 us: 1.00x faster                                                  |
| fannkuch                 | 402 ms                                                     | 400 ms: 1.00x faster                                                  |
| nbody                    | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                                 |
| python_startup_no_site   | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| hexiom                   | 6.30 ms                                                    | 6.28 ms: 1.00x faster                                                 |
| asyncio_tcp              | 508 ms                                                     | 510 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                |
| xml_etree_process        | 61.2 ms                                                    | 61.5 ms: 1.01x slower                                                 |
| sympy_sum                | 156 ms                                                     | 157 ms: 1.01x slower                                                  |
| deltablue                | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                 |
| pprint_safe_repr         | 758 ms                                                     | 764 ms: 1.01x slower                                                  |
| coverage                 | 93.1 ms                                                    | 93.8 ms: 1.01x slower                                                 |
| async_generators         | 442 ms                                                     | 446 ms: 1.01x slower                                                  |
| django_template          | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                 |
| pickle_dict              | 34.8 us                                                    | 35.1 us: 1.01x slower                                                 |
| meteor_contest           | 110 ms                                                     | 111 ms: 1.01x slower                                                  |
| unpickle_pure_python     | 218 us                                                     | 220 us: 1.01x slower                                                  |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| typing_runtime_protocols | 165 us                                                     | 167 us: 1.01x slower                                                  |
| deepcopy_memo            | 39.7 us                                                    | 40.3 us: 1.01x slower                                                 |
| pickle_pure_python       | 305 us                                                     | 310 us: 1.01x slower                                                  |
| pathlib                  | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                 |
| html5lib                 | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                 |
| xml_etree_generate       | 87.4 ms                                                    | 89.0 ms: 1.02x slower                                                 |
| pickle                   | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| scimark_sor              | 127 ms                                                     | 130 ms: 1.02x slower                                                  |
| json                     | 5.31 ms                                                    | 5.44 ms: 1.02x slower                                                 |
| regex_effbot             | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                 |
| pickle_list              | 5.11 us                                                    | 5.29 us: 1.04x slower                                                 |
| async_tree_none_tg       | 336 ms                                                     | 349 ms: 1.04x slower                                                  |
| async_tree_io_tg         | 936 ms                                                     | 981 ms: 1.05x slower                                                  |
| unpickle                 | 15.1 us                                                    | 16.1 us: 1.06x slower                                                 |
| telco                    | 8.41 ms                                                    | 173 ms: 20.59x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (25): flaskblogging, async_tree_cpu_io_mixed_tg, bench_mp_pool, float, thrift, sympy_integrate, bench_thread_pool, unpickle_list, genshi_text, regex_v8, raytrace, xml_etree_iterparse, genshi_xml, json_dumps, pprint_pformat, logging_simple, json_loads, dask, pycparser, xml_etree_parse, pylint, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 88.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x