# Results vs. 3.13.0b2

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: darwin-arm64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.03x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 170 ms: 1.06x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.05x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 215 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.5 ms: 1.03x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.8 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (11): async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.7 ms: 1.02x faster                                                 |
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 64.0 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 72.4 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                  |
| pickle_pure_python   | 179 us                                                     | 172 us: 1.04x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 35.6 ms: 1.04x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.1 ms: 1.02x faster                                                 |
| unpickle_list        | 2.88 us                                                    | 2.85 us: 1.01x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 105 ms: 1.01x faster                                                  |
| pickle_list          | 2.96 us                                                    | 2.94 us: 1.01x faster                                                 |
| pickle               | 7.48 us                                                    | 7.45 us: 1.00x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.30 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.36 ms: 1.10x faster                                                 |
| django_template | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.9 ms: 1.22x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 39.3 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| mako                             | 6.99 ms                                                    | 6.36 ms: 1.10x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 21.9 ms: 1.06x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.06x faster                                                |
| deepcopy_memo                    | 22.6 us                                                    | 21.3 us: 1.06x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                |
| fannkuch                         | 248 ms                                                     | 239 ms: 1.04x faster                                                  |
| pickle_pure_python               | 179 us                                                     | 172 us: 1.04x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 35.6 ms: 1.04x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.47 ms: 1.03x faster                                                 |
| pyflate                          | 321 ms                                                     | 314 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.1 ms: 1.02x faster                                                 |
| float                            | 48.6 ms                                                    | 47.7 ms: 1.02x faster                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.85 us: 1.01x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 460 ms: 1.01x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 105 ms: 1.01x faster                                                  |
| html5lib                         | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| pickle_list                      | 2.96 us                                                    | 2.94 us: 1.01x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.45 us: 1.00x faster                                                 |
| thrift                           | 435 us                                                     | 434 us: 1.00x faster                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.56 us: 1.01x slower                                                 |
| deepcopy                         | 204 us                                                     | 206 us: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 35.6 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.3 ms: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.6 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                 |
| go                               | 101 ms                                                     | 102 ms: 1.02x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.30 us: 1.02x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 914 us: 1.02x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                  |
| generators                       | 22.9 ms                                                    | 23.5 ms: 1.02x slower                                                 |
| async_tree_none                  | 209 ms                                                     | 215 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.5 ms: 1.03x slower                                                 |
| async_generators                 | 281 ms                                                     | 289 ms: 1.03x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.5 ms: 1.03x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.44 us: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.05x slower                                                |
| bench_mp_pool                    | 47.2 ms                                                    | 49.4 ms: 1.05x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 51.8 ms: 1.05x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.5 ms: 1.05x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 72.6 ms: 1.05x slower                                                 |
| sympy_str                        | 131 ms                                                     | 139 ms: 1.05x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 72.4 ms: 1.06x slower                                                 |
| 2to3                             | 161 ms                                                     | 170 ms: 1.06x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.06x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 239 ms: 1.06x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.8 ms: 1.06x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 63.8 ns: 1.06x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.95 ms: 1.06x slower                                                 |
| pycparser                        | 632 ms                                                     | 677 ms: 1.07x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 102 ms: 1.07x slower                                                  |
| nbody                            | 59.6 ms                                                    | 64.0 ms: 1.07x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.2 ms: 1.07x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 483 us: 1.08x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.41 ms: 1.09x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 95.3 us: 1.09x slower                                                 |
| django_template                  | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                                 |
| raytrace                         | 147 ms                                                     | 164 ms: 1.12x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 58.9 ms: 1.13x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.13x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 830 us: 1.13x slower                                                  |
| asyncio_tcp                      | 402 ms                                                     | 457 ms: 1.14x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.47 ms: 1.16x slower                                                 |
| chaos                            | 34.0 ms                                                    | 39.7 ms: 1.17x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 79.1 ms: 1.18x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.21x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.9 ms: 1.22x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 39.3 ms: 1.31x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (20): async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_io, async_tree_none_tg, async_tree_memoization_tg, deepcopy_reduce, json, coroutines, pprint_pformat, asyncio_websockets, regex_dna, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, dask, async_tree_eager_memoization, tornado_http, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, pylint
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.57x