# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.03x slower
- HPT reliability: 74.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                       |
| chameleon      | 7.22 ms                                                    | 7.11 ms: 1.01x faster                                      |
| docutils       | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                     |
| html5lib       | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                      |
| tornado_http   | 94.6 ms                                                    | 95.8 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                      | 1.00x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 363 ms: 1.04x faster                                       |
| async_tree_none_tg | 336 ms                                                     | 346 ms: 1.03x slower                                       |
| async_tree_io_tg   | 936 ms                                                     | 987 ms: 1.05x slower                                       |
| Geometric mean     | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                       |
| nbody          | 88.3 ms                                                    | 87.8 ms: 1.01x faster                                      |
| float          | 78.9 ms                                                    | 78.5 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                       |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                       |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 34.8 us                                                    | 33.8 us: 1.03x faster                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                       |
| xml_etree_process    | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                      |
| xml_etree_generate   | 87.4 ms                                                    | 87.7 ms: 1.00x slower                                      |
| unpickle_list        | 5.34 us                                                    | 5.38 us: 1.01x slower                                      |
| pickle_pure_python   | 305 us                                                     | 311 us: 1.02x slower                                       |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                       |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                      |
| pickle_list          | 5.11 us                                                    | 5.30 us: 1.04x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 2.22 sec: 1.04x slower                                     |
| unpickle             | 15.1 us                                                    | 17.0 us: 1.12x slower                                      |
| Geometric mean       | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                      | 1.00x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.9 ms: 1.03x faster                                      |
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                      |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                      |
| genshi_xml      | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                      | 1.01x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mdp                      | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                     |
| scimark_lu               | 122 ms                                                     | 115 ms: 1.05x faster                                       |
| scimark_fft              | 392 ms                                                     | 373 ms: 1.05x faster                                       |
| chaos                    | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                      |
| async_tree_none          | 378 ms                                                     | 363 ms: 1.04x faster                                       |
| gc_traversal             | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                      |
| mako                     | 11.2 ms                                                    | 10.9 ms: 1.03x faster                                      |
| pickle_dict              | 34.8 us                                                    | 33.8 us: 1.03x faster                                      |
| spectral_norm            | 116 ms                                                     | 113 ms: 1.03x faster                                       |
| thrift                   | 823 us                                                     | 801 us: 1.03x faster                                       |
| deepcopy_reduce          | 3.35 us                                                    | 3.26 us: 1.03x faster                                      |
| coroutines               | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                      |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                      |
| hexiom                   | 6.30 ms                                                    | 6.15 ms: 1.02x faster                                      |
| pyflate                  | 484 ms                                                     | 473 ms: 1.02x faster                                       |
| genshi_text              | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                      |
| fannkuch                 | 402 ms                                                     | 393 ms: 1.02x faster                                       |
| xml_etree_parse          | 162 ms                                                     | 159 ms: 1.02x faster                                       |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.18 ms: 1.02x faster                                      |
| crypto_pyaes             | 77.5 ms                                                    | 76.2 ms: 1.02x faster                                      |
| xml_etree_process        | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                      |
| regex_compile            | 137 ms                                                     | 135 ms: 1.01x faster                                       |
| chameleon                | 7.22 ms                                                    | 7.11 ms: 1.01x faster                                      |
| generators               | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                      |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                       |
| sqlite_synth             | 2.99 us                                                    | 2.96 us: 1.01x faster                                      |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                      |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                      |
| coverage                 | 93.1 ms                                                    | 92.4 ms: 1.01x faster                                      |
| deepcopy_memo            | 39.7 us                                                    | 39.4 us: 1.01x faster                                      |
| richards                 | 50.9 ms                                                    | 50.5 ms: 1.01x faster                                      |
| sqlglot_transpile        | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                      |
| 2to3                     | 274 ms                                                     | 272 ms: 1.01x faster                                       |
| nbody                    | 88.3 ms                                                    | 87.8 ms: 1.01x faster                                      |
| float                    | 78.9 ms                                                    | 78.5 ms: 1.01x faster                                      |
| asyncio_websockets       | 567 ms                                                     | 564 ms: 1.00x faster                                       |
| python_startup           | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                      |
| deepcopy                 | 367 us                                                     | 366 us: 1.00x faster                                       |
| raytrace                 | 267 ms                                                     | 267 ms: 1.00x slower                                       |
| asyncio_tcp              | 508 ms                                                     | 510 ms: 1.00x slower                                       |
| xml_etree_generate       | 87.4 ms                                                    | 87.7 ms: 1.00x slower                                      |
| sqlglot_optimize         | 55.5 ms                                                    | 55.8 ms: 1.01x slower                                      |
| deltablue                | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                      |
| meteor_contest           | 110 ms                                                     | 110 ms: 1.01x slower                                       |
| bench_thread_pool        | 834 us                                                     | 839 us: 1.01x slower                                       |
| unpickle_list            | 5.34 us                                                    | 5.38 us: 1.01x slower                                      |
| django_template          | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                      |
| sympy_expand             | 473 ms                                                     | 477 ms: 1.01x slower                                       |
| pprint_pformat           | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                     |
| gunicorn                 | 1.28 ms                                                    | 1.29 ms: 1.01x slower                                      |
| genshi_xml               | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| sympy_sum                | 156 ms                                                     | 157 ms: 1.01x slower                                       |
| scimark_monte_carlo      | 69.2 ms                                                    | 69.9 ms: 1.01x slower                                      |
| go                       | 145 ms                                                     | 146 ms: 1.01x slower                                       |
| pprint_safe_repr         | 758 ms                                                     | 767 ms: 1.01x slower                                       |
| logging_format           | 6.47 us                                                    | 6.54 us: 1.01x slower                                      |
| docutils                 | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                     |
| python_startup_no_site   | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                      |
| tornado_http             | 94.6 ms                                                    | 95.8 ms: 1.01x slower                                      |
| aiohttp                  | 1.18 ms                                                    | 1.20 ms: 1.01x slower                                      |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                       |
| html5lib                 | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                      |
| pickle_pure_python       | 305 us                                                     | 311 us: 1.02x slower                                       |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                       |
| json                     | 5.31 ms                                                    | 5.41 ms: 1.02x slower                                      |
| comprehensions           | 16.6 us                                                    | 17.0 us: 1.02x slower                                      |
| sqlglot_normalize        | 110 ms                                                     | 113 ms: 1.02x slower                                       |
| unpickle_pure_python     | 218 us                                                     | 223 us: 1.02x slower                                       |
| async_generators         | 442 ms                                                     | 452 ms: 1.02x slower                                       |
| logging_simple           | 5.74 us                                                    | 5.91 us: 1.03x slower                                      |
| typing_runtime_protocols | 165 us                                                     | 170 us: 1.03x slower                                       |
| async_tree_none_tg       | 336 ms                                                     | 346 ms: 1.03x slower                                       |
| pickle                   | 11.5 us                                                    | 11.8 us: 1.03x slower                                      |
| pathlib                  | 17.3 ms                                                    | 17.9 ms: 1.03x slower                                      |
| pickle_list              | 5.11 us                                                    | 5.30 us: 1.04x slower                                      |
| pycparser                | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                     |
| regex_v8                 | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                      |
| tomli_loads              | 2.12 sec                                                   | 2.22 sec: 1.04x slower                                     |
| async_tree_io_tg         | 936 ms                                                     | 987 ms: 1.05x slower                                       |
| unpickle                 | 15.1 us                                                    | 17.0 us: 1.12x slower                                      |
| telco                    | 8.41 ms                                                    | 173 ms: 20.50x slower                                      |
| Geometric mean           | (ref)                                                      | 1.03x slower                                               |

Benchmark hidden because not significant (21): async_tree_io, dulwich_log, richards_super, nqueens, regex_effbot, sympy_integrate, json_loads, asyncio_tcp_ssl, bench_mp_pool, scimark_sor, mypy2, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, flaskblogging, djangocms, sympy_str, dask, async_tree_cpu_io_mixed, pylint, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 74.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x