# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 171 ms                                                                | 176 ms: 1.03x slower                                                  |
| docutils       | 1.51 sec                                                              | 1.55 sec: 1.03x slower                                                |
| html5lib       | 31.0 ms                                                               | 32.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                | 337 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 362 ms                                                                | 369 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 477 ms                                                                | 489 ms: 1.02x slower                                                  |
| async_tree_eager_io              | 758 ms                                                                | 783 ms: 1.03x slower                                                  |
| async_tree_eager_memoization_tg  | 127 ms                                                                | 132 ms: 1.04x slower                                                  |
| async_tree_none                  | 218 ms                                                                | 228 ms: 1.04x slower                                                  |
| async_tree_memoization_tg        | 254 ms                                                                | 266 ms: 1.05x slower                                                  |
| async_tree_none_tg               | 197 ms                                                                | 207 ms: 1.05x slower                                                  |
| async_tree_memoization           | 269 ms                                                                | 282 ms: 1.05x slower                                                  |
| async_tree_eager_tg              | 42.4 ms                                                               | 44.8 ms: 1.06x slower                                                 |
| async_tree_eager                 | 63.3 ms                                                               | 67.4 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.03x slower                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_io_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 63.5 ms                                                               | 63.3 ms: 1.00x faster                                                 |
| float          | 46.6 ms                                                               | 47.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.56 ms                                                               | 2.58 ms: 1.00x slower                                                 |
| regex_v8       | 17.3 ms                                                               | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 72.8 ms                                                               | 74.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 18.2 us                                                               | 18.3 us: 1.01x slower                                                 |
| pickle_list          | 2.95 us                                                               | 2.98 us: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                               | 17.2 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| unpickle             | 9.37 us                                                               | 9.51 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 71.4 ms                                                               | 72.4 ms: 1.01x slower                                                 |
| pickle               | 7.42 us                                                               | 7.55 us: 1.02x slower                                                 |
| tomli_loads          | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                |
| xml_etree_generate   | 51.8 ms                                                               | 53.4 ms: 1.03x slower                                                 |
| pickle_pure_python   | 173 us                                                                | 181 us: 1.04x slower                                                  |
| xml_etree_process    | 36.0 ms                                                               | 37.7 ms: 1.05x slower                                                 |
| unpickle_pure_python | 132 us                                                                | 140 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                               | 13.6 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 40.2 ms                                                               | 36.8 ms: 1.09x faster                                                 |
| mako            | 6.44 ms                                                               | 6.51 ms: 1.01x slower                                                 |
| genshi_text     | 16.1 ms                                                               | 16.5 ms: 1.03x slower                                                 |
| django_template | 21.3 ms                                                               | 23.1 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml                       | 40.2 ms                                                               | 36.8 ms: 1.09x faster                                                 |
| hexiom                           | 4.45 ms                                                               | 4.41 ms: 1.01x faster                                                 |
| spectral_norm                    | 67.5 ms                                                               | 67.1 ms: 1.01x faster                                                 |
| fannkuch                         | 245 ms                                                                | 243 ms: 1.01x faster                                                  |
| nbody                            | 63.5 ms                                                               | 63.3 ms: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                                | 408 ms: 1.00x faster                                                  |
| python_startup_no_site           | 13.6 ms                                                               | 13.6 ms: 1.00x slower                                                 |
| regex_effbot                     | 2.56 ms                                                               | 2.58 ms: 1.00x slower                                                 |
| sqlite_synth                     | 1.57 us                                                               | 1.58 us: 1.01x slower                                                 |
| pickle_dict                      | 18.2 us                                                               | 18.3 us: 1.01x slower                                                 |
| telco                            | 4.60 ms                                                               | 4.63 ms: 1.01x slower                                                 |
| scimark_fft                      | 185 ms                                                                | 187 ms: 1.01x slower                                                  |
| regex_v8                         | 17.3 ms                                                               | 17.4 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                               | 3.00 ms: 1.01x slower                                                 |
| deepcopy_memo                    | 16.8 us                                                               | 17.0 us: 1.01x slower                                                 |
| json                             | 2.92 ms                                                               | 2.94 ms: 1.01x slower                                                 |
| pickle_list                      | 2.95 us                                                               | 2.98 us: 1.01x slower                                                 |
| mako                             | 6.44 ms                                                               | 6.51 ms: 1.01x slower                                                 |
| json_loads                       | 17.0 us                                                               | 17.2 us: 1.01x slower                                                 |
| xml_etree_parse                  | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| meteor_contest                   | 71.7 ms                                                               | 72.7 ms: 1.01x slower                                                 |
| unpickle                         | 9.37 us                                                               | 9.51 us: 1.01x slower                                                 |
| pyflate                          | 314 ms                                                                | 318 ms: 1.01x slower                                                  |
| pycparser                        | 677 ms                                                                | 687 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.4 ms                                                               | 72.4 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                | 337 ms: 1.02x slower                                                  |
| create_gc_cycles                 | 897 us                                                                | 912 us: 1.02x slower                                                  |
| regex_compile                    | 72.8 ms                                                               | 74.1 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 362 ms                                                                | 369 ms: 1.02x slower                                                  |
| pickle                           | 7.42 us                                                               | 7.55 us: 1.02x slower                                                 |
| float                            | 46.6 ms                                                               | 47.4 ms: 1.02x slower                                                 |
| comprehensions                   | 12.2 us                                                               | 12.5 us: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.12 sec                                                              | 3.18 sec: 1.02x slower                                                |
| scimark_monte_carlo              | 43.6 ms                                                               | 44.5 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 51.5 ms                                                               | 52.5 ms: 1.02x slower                                                 |
| pprint_pformat                   | 966 ms                                                                | 988 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 50.3 ms                                                               | 51.5 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed          | 477 ms                                                                | 489 ms: 1.02x slower                                                  |
| tomli_loads                      | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                |
| mdp                              | 1.45 sec                                                              | 1.49 sec: 1.03x slower                                                |
| sympy_sum                        | 73.4 ms                                                               | 75.4 ms: 1.03x slower                                                 |
| docutils                         | 1.51 sec                                                              | 1.55 sec: 1.03x slower                                                |
| genshi_text                      | 16.1 ms                                                               | 16.5 ms: 1.03x slower                                                 |
| xml_etree_generate               | 51.8 ms                                                               | 53.4 ms: 1.03x slower                                                 |
| nqueens                          | 58.2 ms                                                               | 60.0 ms: 1.03x slower                                                 |
| 2to3                             | 171 ms                                                                | 176 ms: 1.03x slower                                                  |
| async_generators                 | 297 ms                                                                | 306 ms: 1.03x slower                                                  |
| async_tree_eager_io              | 758 ms                                                                | 783 ms: 1.03x slower                                                  |
| deepcopy                         | 153 us                                                                | 158 us: 1.03x slower                                                  |
| sympy_integrate                  | 11.0 ms                                                               | 11.4 ms: 1.04x slower                                                 |
| bench_thread_pool                | 472 us                                                                | 489 us: 1.04x slower                                                  |
| typing_runtime_protocols         | 95.3 us                                                               | 98.8 us: 1.04x slower                                                 |
| dask                             | 223 ms                                                                | 231 ms: 1.04x slower                                                  |
| html5lib                         | 31.0 ms                                                               | 32.1 ms: 1.04x slower                                                 |
| async_tree_eager_memoization_tg  | 127 ms                                                                | 132 ms: 1.04x slower                                                  |
| sympy_str                        | 139 ms                                                                | 145 ms: 1.04x slower                                                  |
| go                               | 101 ms                                                                | 106 ms: 1.04x slower                                                  |
| sqlglot_optimize                 | 33.1 ms                                                               | 34.5 ms: 1.04x slower                                                 |
| async_tree_none                  | 218 ms                                                                | 228 ms: 1.04x slower                                                  |
| logging_silent                   | 62.6 ns                                                               | 65.4 ns: 1.04x slower                                                 |
| pickle_pure_python               | 173 us                                                                | 181 us: 1.04x slower                                                  |
| async_tree_memoization_tg        | 254 ms                                                                | 266 ms: 1.05x slower                                                  |
| async_tree_none_tg               | 197 ms                                                                | 207 ms: 1.05x slower                                                  |
| pprint_safe_repr                 | 463 ms                                                                | 485 ms: 1.05x slower                                                  |
| xml_etree_process                | 36.0 ms                                                               | 37.7 ms: 1.05x slower                                                 |
| sympy_expand                     | 241 ms                                                                | 252 ms: 1.05x slower                                                  |
| async_tree_memoization           | 269 ms                                                                | 282 ms: 1.05x slower                                                  |
| scimark_sor                      | 102 ms                                                                | 107 ms: 1.05x slower                                                  |
| sqlglot_transpile                | 998 us                                                                | 1.05 ms: 1.05x slower                                                 |
| chaos                            | 39.4 ms                                                               | 41.5 ms: 1.05x slower                                                 |
| coverage                         | 45.5 ms                                                               | 48.0 ms: 1.05x slower                                                 |
| deepcopy_reduce                  | 1.53 us                                                               | 1.62 us: 1.06x slower                                                 |
| thrift                           | 438 us                                                                | 462 us: 1.06x slower                                                  |
| async_tree_eager_tg              | 42.4 ms                                                               | 44.8 ms: 1.06x slower                                                 |
| sqlglot_parse                    | 822 us                                                                | 871 us: 1.06x slower                                                  |
| unpickle_pure_python             | 132 us                                                                | 140 us: 1.06x slower                                                  |
| gc_traversal                     | 2.46 ms                                                               | 2.61 ms: 1.06x slower                                                 |
| async_tree_eager                 | 63.3 ms                                                               | 67.4 ms: 1.06x slower                                                 |
| asyncio_tcp                      | 414 ms                                                                | 443 ms: 1.07x slower                                                  |
| richards                         | 31.5 ms                                                               | 33.9 ms: 1.08x slower                                                 |
| logging_format                   | 3.29 us                                                               | 3.55 us: 1.08x slower                                                 |
| logging_simple                   | 3.01 us                                                               | 3.26 us: 1.08x slower                                                 |
| scimark_lu                       | 79.7 ms                                                               | 86.3 ms: 1.08x slower                                                 |
| deltablue                        | 2.37 ms                                                               | 2.57 ms: 1.08x slower                                                 |
| django_template                  | 21.3 ms                                                               | 23.1 ms: 1.09x slower                                                 |
| richards_super                   | 35.3 ms                                                               | 38.5 ms: 1.09x slower                                                 |
| raytrace                         | 162 ms                                                                | 182 ms: 1.12x slower                                                  |
| generators                       | 23.2 ms                                                               | 26.3 ms: 1.13x slower                                                 |
| coroutines                       | 16.0 ms                                                               | 18.3 ms: 1.14x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.03x slower                                                          |

Benchmark hidden because not significant (14): asyncio_tcp_ssl, regex_dna, pidigits, json_dumps, unpickle_list, pathlib, python_startup, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_io_tg, tornado_http, pylint, async_tree_eager_memoization
Ignored benchmarks (1) of results/bm-20240618-3.14.0a0-9f741e5-JIT/bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.97x