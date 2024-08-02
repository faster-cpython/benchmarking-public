# Results vs. 3.13.0b2

- fork: saulshanabrook
- ref: optimzer_type_versio
- machine: linux-x86_64
- commit hash: 1520928
- commit date: 2024-05-20
- overall geometric mean: 1.00x faster
- HPT reliability: 92.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                          |
| chameleon      | 7.22 ms                                                    | 7.04 ms: 1.03x faster                                                         |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                        |
| html5lib       | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                                         |
| tornado_http   | 94.6 ms                                                    | 97.0 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.4 ms: 1.09x faster                                                         |
| nbody          | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                                         |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 25.2 ms: 1.01x slower                                                         |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                          |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                          |
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 83.0 ms: 1.05x faster                                                         |
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                                         |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.03x faster                                                          |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                         |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                                          |
| pickle_dict          | 34.8 us                                                    | 36.1 us: 1.04x slower                                                         |
| pickle_list          | 5.11 us                                                    | 5.38 us: 1.05x slower                                                         |
| pickle               | 11.5 us                                                    | 12.1 us: 1.06x slower                                                         |
| unpickle             | 15.1 us                                                    | 16.7 us: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.02x slower                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                         |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.99 ms: 1.13x faster                                                         |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                         |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                         |
| genshi_xml      | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                         |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|--------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 318 ms: 1.24x faster                                                          |
| richards                 | 50.9 ms                                                    | 41.3 ms: 1.23x faster                                                         |
| richards_super           | 57.4 ms                                                    | 47.5 ms: 1.21x faster                                                         |
| spectral_norm            | 116 ms                                                     | 100 ms: 1.16x faster                                                          |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.54 ms: 1.16x faster                                                         |
| crypto_pyaes             | 77.5 ms                                                    | 68.5 ms: 1.13x faster                                                         |
| mako                     | 11.2 ms                                                    | 9.99 ms: 1.13x faster                                                         |
| fannkuch                 | 402 ms                                                     | 361 ms: 1.11x faster                                                          |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                                         |
| float                    | 78.9 ms                                                    | 72.4 ms: 1.09x faster                                                         |
| nbody                    | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                                         |
| pprint_safe_repr         | 758 ms                                                     | 701 ms: 1.08x faster                                                          |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                        |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                        |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                          |
| xml_etree_parse          | 162 ms                                                     | 153 ms: 1.06x faster                                                          |
| deepcopy_memo            | 39.7 us                                                    | 37.7 us: 1.05x faster                                                         |
| xml_etree_generate       | 87.4 ms                                                    | 83.0 ms: 1.05x faster                                                         |
| pathlib                  | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                         |
| xml_etree_process        | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                                         |
| sqlite_synth             | 2.99 us                                                    | 2.87 us: 1.04x faster                                                         |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| pickle_pure_python       | 305 us                                                     | 295 us: 1.03x faster                                                          |
| pyflate                  | 484 ms                                                     | 470 ms: 1.03x faster                                                          |
| logging_format           | 6.47 us                                                    | 6.31 us: 1.03x faster                                                         |
| chameleon                | 7.22 ms                                                    | 7.04 ms: 1.03x faster                                                         |
| telco                    | 8.41 ms                                                    | 8.23 ms: 1.02x faster                                                         |
| deepcopy_reduce          | 3.35 us                                                    | 3.28 us: 1.02x faster                                                         |
| chaos                    | 61.3 ms                                                    | 60.1 ms: 1.02x faster                                                         |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                          |
| logging_simple           | 5.74 us                                                    | 5.65 us: 1.02x faster                                                         |
| gc_traversal             | 3.98 ms                                                    | 3.92 ms: 1.01x faster                                                         |
| json                     | 5.31 ms                                                    | 5.23 ms: 1.01x faster                                                         |
| deepcopy                 | 367 us                                                     | 364 us: 1.01x faster                                                          |
| json_loads               | 28.9 us                                                    | 28.6 us: 1.01x faster                                                         |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                         |
| thrift                   | 823 us                                                     | 816 us: 1.01x faster                                                          |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                                          |
| regex_v8                 | 25.1 ms                                                    | 25.2 ms: 1.01x slower                                                         |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                         |
| bench_mp_pool            | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                                         |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                         |
| scimark_lu               | 122 ms                                                     | 123 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                        |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.02x slower                                                         |
| html5lib                 | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                                         |
| regex_compile            | 137 ms                                                     | 140 ms: 1.02x slower                                                          |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                          |
| generators               | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                                         |
| unpickle_pure_python     | 218 us                                                     | 223 us: 1.02x slower                                                          |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                                          |
| flaskblogging            | 9.01 ms                                                    | 9.22 ms: 1.02x slower                                                         |
| tornado_http             | 94.6 ms                                                    | 97.0 ms: 1.02x slower                                                         |
| go                       | 145 ms                                                     | 148 ms: 1.03x slower                                                          |
| sqlglot_optimize         | 55.5 ms                                                    | 57.0 ms: 1.03x slower                                                         |
| dask                     | 369 ms                                                     | 380 ms: 1.03x slower                                                          |
| typing_runtime_protocols | 165 us                                                     | 170 us: 1.03x slower                                                          |
| logging_silent           | 105 ns                                                     | 108 ns: 1.03x slower                                                          |
| dulwich_log              | 67.2 ms                                                    | 69.5 ms: 1.03x slower                                                         |
| coroutines               | 23.2 ms                                                    | 24.0 ms: 1.04x slower                                                         |
| asyncio_tcp              | 508 ms                                                     | 526 ms: 1.04x slower                                                          |
| bench_thread_pool        | 834 us                                                     | 865 us: 1.04x slower                                                          |
| pickle_dict              | 34.8 us                                                    | 36.1 us: 1.04x slower                                                         |
| genshi_text              | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                         |
| sqlglot_normalize        | 110 ms                                                     | 115 ms: 1.04x slower                                                          |
| raytrace                 | 267 ms                                                     | 278 ms: 1.04x slower                                                          |
| pycparser                | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                        |
| async_generators         | 442 ms                                                     | 461 ms: 1.04x slower                                                          |
| docutils                 | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                        |
| django_template          | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                         |
| pickle_list              | 5.11 us                                                    | 5.38 us: 1.05x slower                                                         |
| nqueens                  | 81.4 ms                                                    | 85.9 ms: 1.06x slower                                                         |
| pickle                   | 11.5 us                                                    | 12.1 us: 1.06x slower                                                         |
| scimark_sor              | 127 ms                                                     | 137 ms: 1.07x slower                                                          |
| python_startup_no_site   | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                         |
| sympy_str                | 282 ms                                                     | 303 ms: 1.07x slower                                                          |
| sympy_expand             | 473 ms                                                     | 512 ms: 1.08x slower                                                          |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                         |
| unpickle                 | 15.1 us                                                    | 16.7 us: 1.10x slower                                                         |
| sympy_sum                | 156 ms                                                     | 172 ms: 1.10x slower                                                          |
| pylint                   | 317 ms                                                     | 355 ms: 1.12x slower                                                          |
| genshi_xml               | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                         |
| deltablue                | 3.25 ms                                                    | 3.75 ms: 1.15x slower                                                         |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                                  |

Benchmark hidden because not significant (13): unpickle_list, create_gc_cycles, async_tree_cpu_io_mixed_tg, regex_effbot, asyncio_websockets, async_tree_io, async_tree_none_tg, coverage, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_io_tg
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, hexiom, mdp, mypy2

# HPT report

- Reliability score: 92.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x