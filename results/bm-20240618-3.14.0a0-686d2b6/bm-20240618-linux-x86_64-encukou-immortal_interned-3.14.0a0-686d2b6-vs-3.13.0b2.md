# Results vs. 3.13.0b2

- fork: encukou
- ref: immortal_interned
- machine: linux-x86_64
- commit hash: 686d2b6
- commit date: 2024-06-18
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                |
| docutils       | 2.83 sec                                                   | 2.79 sec: 1.01x faster                                              |
| html5lib       | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                               |
| tornado_http   | 94.6 ms                                                    | 94.2 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                      | 1.00x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                               |
| float          | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                               |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                               |
| regex_effbot   | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                               |
| regex_dna      | 221 ms                                                     | 235 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.18 us: 1.03x faster                                               |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                |
| pickle_list          | 5.11 us                                                    | 5.00 us: 1.02x faster                                               |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                               |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.02x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 60.9 ms: 1.00x faster                                               |
| xml_etree_generate   | 87.4 ms                                                    | 87.2 ms: 1.00x faster                                               |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                                |
| json_dumps           | 10.7 ms                                                    | 10.9 ms: 1.01x slower                                               |
| pickle_dict          | 34.8 us                                                    | 35.6 us: 1.02x slower                                               |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                      | 1.00x faster                                                        |

Benchmark hidden because not significant (2): tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                               |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 50.4 ms: 1.02x faster                                               |
| genshi_text     | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                               |
| django_template | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                               |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy                 | 367 us                                                     | 267 us: 1.37x faster                                                |
| deepcopy_memo            | 39.7 us                                                    | 29.7 us: 1.34x faster                                               |
| deepcopy_reduce          | 3.35 us                                                    | 2.72 us: 1.23x faster                                               |
| pathlib                  | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                               |
| scimark_fft              | 392 ms                                                     | 367 ms: 1.07x faster                                                |
| scimark_lu               | 122 ms                                                     | 114 ms: 1.06x faster                                                |
| gc_traversal             | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                               |
| richards                 | 50.9 ms                                                    | 48.9 ms: 1.04x faster                                               |
| create_gc_cycles         | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                               |
| crypto_pyaes             | 77.5 ms                                                    | 74.8 ms: 1.04x faster                                               |
| fannkuch                 | 402 ms                                                     | 388 ms: 1.03x faster                                                |
| richards_super           | 57.4 ms                                                    | 55.5 ms: 1.03x faster                                               |
| regex_compile            | 137 ms                                                     | 133 ms: 1.03x faster                                                |
| unpickle_list            | 5.34 us                                                    | 5.18 us: 1.03x faster                                               |
| xml_etree_parse          | 162 ms                                                     | 157 ms: 1.03x faster                                                |
| dulwich_log              | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                               |
| bpe_tokeniser            | 5.02 sec                                                   | 4.90 sec: 1.03x faster                                              |
| mdp                      | 2.79 sec                                                   | 2.72 sec: 1.02x faster                                              |
| thrift                   | 823 us                                                     | 804 us: 1.02x faster                                                |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.15 ms: 1.02x faster                                               |
| genshi_xml               | 51.6 ms                                                    | 50.4 ms: 1.02x faster                                               |
| asyncio_tcp              | 508 ms                                                     | 497 ms: 1.02x faster                                                |
| scimark_monte_carlo      | 69.2 ms                                                    | 67.7 ms: 1.02x faster                                               |
| pickle_list              | 5.11 us                                                    | 5.00 us: 1.02x faster                                               |
| nbody                    | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                               |
| json_loads               | 28.9 us                                                    | 28.3 us: 1.02x faster                                               |
| hexiom                   | 6.30 ms                                                    | 6.18 ms: 1.02x faster                                               |
| unpickle_pure_python     | 218 us                                                     | 214 us: 1.02x faster                                                |
| json                     | 5.31 ms                                                    | 5.21 ms: 1.02x faster                                               |
| sqlglot_optimize         | 55.5 ms                                                    | 54.6 ms: 1.02x faster                                               |
| pprint_safe_repr         | 758 ms                                                     | 745 ms: 1.02x faster                                                |
| pprint_pformat           | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                              |
| xml_etree_iterparse      | 107 ms                                                     | 106 ms: 1.02x faster                                                |
| typing_runtime_protocols | 165 us                                                     | 162 us: 1.02x faster                                                |
| genshi_text              | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                               |
| float                    | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                               |
| docutils                 | 2.83 sec                                                   | 2.79 sec: 1.01x faster                                              |
| spectral_norm            | 116 ms                                                     | 115 ms: 1.01x faster                                                |
| nqueens                  | 81.4 ms                                                    | 80.3 ms: 1.01x faster                                               |
| sqlite_synth             | 2.99 us                                                    | 2.95 us: 1.01x faster                                               |
| pyflate                  | 484 ms                                                     | 478 ms: 1.01x faster                                                |
| sympy_integrate          | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                               |
| telco                    | 8.41 ms                                                    | 8.32 ms: 1.01x faster                                               |
| sqlglot_normalize        | 110 ms                                                     | 109 ms: 1.01x faster                                                |
| sympy_sum                | 156 ms                                                     | 154 ms: 1.01x faster                                                |
| sympy_str                | 282 ms                                                     | 279 ms: 1.01x faster                                                |
| coroutines               | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                               |
| pidigits                 | 191 ms                                                     | 190 ms: 1.01x faster                                                |
| sqlglot_transpile        | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                               |
| generators               | 29.6 ms                                                    | 29.5 ms: 1.01x faster                                               |
| django_template          | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                               |
| tornado_http             | 94.6 ms                                                    | 94.2 ms: 1.00x faster                                               |
| async_generators         | 442 ms                                                     | 440 ms: 1.00x faster                                                |
| 2to3                     | 274 ms                                                     | 273 ms: 1.00x faster                                                |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.83 sec: 1.00x faster                                              |
| xml_etree_process        | 61.2 ms                                                    | 60.9 ms: 1.00x faster                                               |
| logging_silent           | 105 ns                                                     | 104 ns: 1.00x faster                                                |
| xml_etree_generate       | 87.4 ms                                                    | 87.2 ms: 1.00x faster                                               |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.00x faster                                                |
| python_startup           | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                               |
| go                       | 145 ms                                                     | 145 ms: 1.00x slower                                                |
| deltablue                | 3.25 ms                                                    | 3.27 ms: 1.00x slower                                               |
| coverage                 | 93.1 ms                                                    | 93.8 ms: 1.01x slower                                               |
| pickle_pure_python       | 305 us                                                     | 308 us: 1.01x slower                                                |
| mako                     | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                               |
| python_startup_no_site   | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                               |
| logging_simple           | 5.74 us                                                    | 5.82 us: 1.01x slower                                               |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                               |
| json_dumps               | 10.7 ms                                                    | 10.9 ms: 1.01x slower                                               |
| html5lib                 | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                               |
| pickle_dict              | 34.8 us                                                    | 35.6 us: 1.02x slower                                               |
| pycparser                | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                              |
| regex_v8                 | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                               |
| pickle                   | 11.5 us                                                    | 11.9 us: 1.04x slower                                               |
| regex_effbot             | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                               |
| scimark_sor              | 127 ms                                                     | 133 ms: 1.04x slower                                                |
| regex_dna                | 221 ms                                                     | 235 ms: 1.06x slower                                                |
| Geometric mean           | (ref)                                                      | 1.02x faster                                                        |

Benchmark hidden because not significant (20): async_tree_memoization_tg, async_tree_none, dask, async_tree_none_tg, sympy_expand, bench_thread_pool, pylint, async_tree_memoization, tomli_loads, raytrace, chaos, sqlglot_parse, asyncio_websockets, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_io_tg, logging_format, async_tree_io, unpickle, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x