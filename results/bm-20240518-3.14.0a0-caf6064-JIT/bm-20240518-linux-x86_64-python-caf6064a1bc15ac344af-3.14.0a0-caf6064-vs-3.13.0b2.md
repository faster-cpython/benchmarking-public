# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x slower
- HPT reliability: 51.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                  |
| chameleon      | 7.22 ms                                                    | 7.06 ms: 1.02x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.94 sec: 1.04x slower                                                |
| html5lib       | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 96.6 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 363 ms: 1.04x faster                                                  |
| async_tree_none_tg | 336 ms                                                     | 350 ms: 1.04x slower                                                  |
| async_tree_io_tg   | 936 ms                                                     | 986 ms: 1.05x slower                                                  |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                 |
| float          | 78.9 ms                                                    | 71.9 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 209 ms: 1.06x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.47 ms: 1.06x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.04x faster                                                 |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 151 ms: 1.07x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 82.4 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.06x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.38 us: 1.01x slower                                                 |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                  |
| pickle_list          | 5.11 us                                                    | 5.57 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.62 ms: 1.17x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                 |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 313 ms: 1.25x faster                                                  |
| richards                 | 50.9 ms                                                    | 42.1 ms: 1.21x faster                                                 |
| richards_super           | 57.4 ms                                                    | 48.0 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.45 ms: 1.18x faster                                                 |
| mako                     | 11.2 ms                                                    | 9.62 ms: 1.17x faster                                                 |
| crypto_pyaes             | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                 |
| spectral_norm            | 116 ms                                                     | 101 ms: 1.15x faster                                                  |
| fannkuch                 | 402 ms                                                     | 359 ms: 1.12x faster                                                  |
| pyflate                  | 484 ms                                                     | 437 ms: 1.11x faster                                                  |
| nbody                    | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                 |
| float                    | 78.9 ms                                                    | 71.9 ms: 1.10x faster                                                 |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.1 ms: 1.10x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                |
| mdp                      | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                                |
| xml_etree_parse          | 162 ms                                                     | 151 ms: 1.07x faster                                                  |
| xml_etree_generate       | 87.4 ms                                                    | 82.4 ms: 1.06x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| regex_dna                | 221 ms                                                     | 209 ms: 1.06x faster                                                  |
| regex_effbot             | 3.67 ms                                                    | 3.47 ms: 1.06x faster                                                 |
| xml_etree_iterparse      | 107 ms                                                     | 102 ms: 1.06x faster                                                  |
| xml_etree_process        | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                                 |
| deepcopy_memo            | 39.7 us                                                    | 37.7 us: 1.05x faster                                                 |
| pprint_safe_repr         | 758 ms                                                     | 721 ms: 1.05x faster                                                  |
| pathlib                  | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                 |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.05x faster                                                 |
| regex_v8                 | 25.1 ms                                                    | 24.0 ms: 1.04x faster                                                 |
| async_tree_none          | 378 ms                                                     | 363 ms: 1.04x faster                                                  |
| gc_traversal             | 3.98 ms                                                    | 3.84 ms: 1.04x faster                                                 |
| chaos                    | 61.3 ms                                                    | 59.5 ms: 1.03x faster                                                 |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.31 us: 1.03x faster                                                 |
| chameleon                | 7.22 ms                                                    | 7.06 ms: 1.02x faster                                                 |
| html5lib                 | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                 |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| pickle_dict              | 34.8 us                                                    | 34.2 us: 1.02x faster                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                 |
| deepcopy_reduce          | 3.35 us                                                    | 3.31 us: 1.01x faster                                                 |
| logging_simple           | 5.74 us                                                    | 5.69 us: 1.01x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                    | 1.63 ms: 1.00x faster                                                 |
| create_gc_cycles         | 1.82 ms                                                    | 1.82 ms: 1.00x slower                                                 |
| unpickle_list            | 5.34 us                                                    | 5.38 us: 1.01x slower                                                 |
| pickle                   | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                  |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                 |
| generators               | 29.6 ms                                                    | 30.0 ms: 1.01x slower                                                 |
| go                       | 145 ms                                                     | 147 ms: 1.01x slower                                                  |
| meteor_contest           | 110 ms                                                     | 112 ms: 1.02x slower                                                  |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                  |
| flaskblogging            | 9.01 ms                                                    | 9.18 ms: 1.02x slower                                                 |
| tornado_http             | 94.6 ms                                                    | 96.6 ms: 1.02x slower                                                 |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                  |
| dask                     | 369 ms                                                     | 378 ms: 1.02x slower                                                  |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                                  |
| asyncio_tcp              | 508 ms                                                     | 522 ms: 1.03x slower                                                  |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                 |
| logging_silent           | 105 ns                                                     | 108 ns: 1.03x slower                                                  |
| coverage                 | 93.1 ms                                                    | 95.9 ms: 1.03x slower                                                 |
| raytrace                 | 267 ms                                                     | 275 ms: 1.03x slower                                                  |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                  |
| bench_thread_pool        | 834 us                                                     | 860 us: 1.03x slower                                                  |
| dulwich_log              | 67.2 ms                                                    | 69.5 ms: 1.04x slower                                                 |
| docutils                 | 2.83 sec                                                   | 2.94 sec: 1.04x slower                                                |
| async_tree_none_tg       | 336 ms                                                     | 350 ms: 1.04x slower                                                  |
| async_generators         | 442 ms                                                     | 462 ms: 1.04x slower                                                  |
| scimark_sor              | 127 ms                                                     | 133 ms: 1.05x slower                                                  |
| genshi_text              | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                 |
| typing_runtime_protocols | 165 us                                                     | 173 us: 1.05x slower                                                  |
| async_tree_io_tg         | 936 ms                                                     | 986 ms: 1.05x slower                                                  |
| django_template          | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                 |
| hexiom                   | 6.30 ms                                                    | 6.68 ms: 1.06x slower                                                 |
| sympy_str                | 282 ms                                                     | 300 ms: 1.06x slower                                                  |
| python_startup_no_site   | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                 |
| nqueens                  | 81.4 ms                                                    | 87.3 ms: 1.07x slower                                                 |
| sympy_expand             | 473 ms                                                     | 508 ms: 1.07x slower                                                  |
| pickle_list              | 5.11 us                                                    | 5.57 us: 1.09x slower                                                 |
| sympy_sum                | 156 ms                                                     | 171 ms: 1.10x slower                                                  |
| sympy_integrate          | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                 |
| pylint                   | 317 ms                                                     | 352 ms: 1.11x slower                                                  |
| genshi_xml               | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                 |
| deltablue                | 3.25 ms                                                    | 3.71 ms: 1.14x slower                                                 |
| telco                    | 8.41 ms                                                    | 172 ms: 20.41x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (15): pycparser, deepcopy, json_loads, thrift, coroutines, asyncio_websockets, json, comprehensions, bench_mp_pool, unpickle, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 51.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x