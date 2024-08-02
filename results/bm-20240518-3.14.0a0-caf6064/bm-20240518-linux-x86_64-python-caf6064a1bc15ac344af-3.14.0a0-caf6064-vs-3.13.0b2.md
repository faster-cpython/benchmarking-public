# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 268 ms: 1.02x faster                                                  |
| chameleon      | 7.22 ms                                                    | 6.97 ms: 1.04x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none  | 378 ms                                                     | 362 ms: 1.05x faster                                                  |
| async_tree_io_tg | 936 ms                                                     | 969 ms: 1.03x slower                                                  |
| Geometric mean   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.2 ms: 1.02x faster                                                 |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                  |
| nbody          | 88.3 ms                                                    | 87.2 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                 |
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 60.1 ms: 1.02x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                                |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                  |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.47 us: 1.02x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.61 us: 1.10x slower                                                 |
| unpickle             | 15.1 us                                                    | 16.9 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_dumps, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.4 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                 |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 51.0 ms: 1.01x faster                                                 |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                      | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                                |
| richards                 | 50.9 ms                                                    | 48.0 ms: 1.06x faster                                                 |
| pathlib                  | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                 |
| crypto_pyaes             | 77.5 ms                                                    | 73.4 ms: 1.05x faster                                                 |
| richards_super           | 57.4 ms                                                    | 54.5 ms: 1.05x faster                                                 |
| async_tree_none          | 378 ms                                                     | 362 ms: 1.05x faster                                                  |
| spectral_norm            | 116 ms                                                     | 111 ms: 1.04x faster                                                  |
| scimark_lu               | 122 ms                                                     | 117 ms: 1.04x faster                                                  |
| scimark_fft              | 392 ms                                                     | 377 ms: 1.04x faster                                                  |
| python_startup           | 10.8 ms                                                    | 10.4 ms: 1.04x faster                                                 |
| chameleon                | 7.22 ms                                                    | 6.97 ms: 1.04x faster                                                 |
| regex_effbot             | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.11 ms: 1.03x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.29 us: 1.03x faster                                                 |
| logging_silent           | 105 ns                                                     | 102 ns: 1.03x faster                                                  |
| genshi_text              | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                 |
| chaos                    | 61.3 ms                                                    | 59.8 ms: 1.03x faster                                                 |
| deepcopy_reduce          | 3.35 us                                                    | 3.26 us: 1.03x faster                                                 |
| html5lib                 | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| nqueens                  | 81.4 ms                                                    | 79.6 ms: 1.02x faster                                                 |
| float                    | 78.9 ms                                                    | 77.2 ms: 1.02x faster                                                 |
| 2to3                     | 274 ms                                                     | 268 ms: 1.02x faster                                                  |
| xml_etree_parse          | 162 ms                                                     | 158 ms: 1.02x faster                                                  |
| thrift                   | 823 us                                                     | 806 us: 1.02x faster                                                  |
| gc_traversal             | 3.98 ms                                                    | 3.90 ms: 1.02x faster                                                 |
| regex_compile            | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| xml_etree_process        | 61.2 ms                                                    | 60.1 ms: 1.02x faster                                                 |
| deepcopy                 | 367 us                                                     | 361 us: 1.02x faster                                                  |
| docutils                 | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                |
| deepcopy_memo            | 39.7 us                                                    | 39.1 us: 1.02x faster                                                 |
| sqlglot_optimize         | 55.5 ms                                                    | 54.7 ms: 1.02x faster                                                 |
| pickle_dict              | 34.8 us                                                    | 34.2 us: 1.02x faster                                                 |
| django_template          | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                 |
| sqlglot_normalize        | 110 ms                                                     | 109 ms: 1.01x faster                                                  |
| sqlite_synth             | 2.99 us                                                    | 2.95 us: 1.01x faster                                                 |
| sympy_str                | 282 ms                                                     | 278 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                  |
| sympy_expand             | 473 ms                                                     | 467 ms: 1.01x faster                                                  |
| flaskblogging            | 9.01 ms                                                    | 8.89 ms: 1.01x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                |
| nbody                    | 88.3 ms                                                    | 87.2 ms: 1.01x faster                                                 |
| xml_etree_generate       | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                 |
| dulwich_log              | 67.2 ms                                                    | 66.4 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                 |
| genshi_xml               | 51.6 ms                                                    | 51.0 ms: 1.01x faster                                                 |
| regex_dna                | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| scimark_monte_carlo      | 69.2 ms                                                    | 68.4 ms: 1.01x faster                                                 |
| sympy_integrate          | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                                 |
| pprint_safe_repr         | 758 ms                                                     | 751 ms: 1.01x faster                                                  |
| pyflate                  | 484 ms                                                     | 480 ms: 1.01x faster                                                  |
| mako                     | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                 |
| tornado_http             | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                                |
| sympy_sum                | 156 ms                                                     | 155 ms: 1.00x faster                                                  |
| asyncio_tcp              | 508 ms                                                     | 506 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.84 sec: 1.00x faster                                                |
| meteor_contest           | 110 ms                                                     | 111 ms: 1.01x slower                                                  |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| async_generators         | 442 ms                                                     | 447 ms: 1.01x slower                                                  |
| unpickle_pure_python     | 218 us                                                     | 220 us: 1.01x slower                                                  |
| deltablue                | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                 |
| typing_runtime_protocols | 165 us                                                     | 167 us: 1.01x slower                                                  |
| json                     | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                                 |
| regex_v8                 | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                 |
| pickle                   | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| unpickle_list            | 5.34 us                                                    | 5.47 us: 1.02x slower                                                 |
| pycparser                | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                |
| async_tree_io_tg         | 936 ms                                                     | 969 ms: 1.03x slower                                                  |
| pickle_list              | 5.11 us                                                    | 5.61 us: 1.10x slower                                                 |
| unpickle                 | 15.1 us                                                    | 16.9 us: 1.12x slower                                                 |
| telco                    | 8.41 ms                                                    | 173 ms: 20.62x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (26): async_tree_cpu_io_mixed_tg, scimark_sor, coverage, xml_etree_iterparse, logging_simple, bench_mp_pool, raytrace, bench_thread_pool, json_dumps, pickle_pure_python, coroutines, dask, json_loads, python_startup_no_site, fannkuch, asyncio_websockets, hexiom, create_gc_cycles, pylint, generators, go, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x