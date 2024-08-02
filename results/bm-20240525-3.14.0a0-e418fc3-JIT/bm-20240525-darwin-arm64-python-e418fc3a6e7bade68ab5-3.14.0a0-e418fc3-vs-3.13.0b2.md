# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| chameleon      | 4.27 ms                                                    | 4.42 ms: 1.04x slower                                                 |
| docutils       | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 358 ms                                                     | 360 ms: 1.01x slower                                                  |
| async_tree_eager_tg           | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                 |
| async_tree_none               | 209 ms                                                     | 216 ms: 1.03x slower                                                  |
| async_tree_eager              | 60.3 ms                                                    | 64.0 ms: 1.06x slower                                                 |
| Geometric mean                | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.3 ms: 1.03x faster                                                 |
| nbody          | 59.6 ms                                                    | 63.7 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.5 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 72.4 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 35.7 ms: 1.04x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 172 us: 1.04x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 51.2 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.2 ms: 1.02x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| json_dumps           | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| pickle               | 7.48 us                                                    | 7.44 us: 1.01x faster                                                 |
| unpickle_list        | 2.88 us                                                    | 2.89 us: 1.00x slower                                                 |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.01x slower                                                 |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.27 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.9 ms: 1.05x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.3 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.37 ms: 1.10x faster                                                 |
| django_template | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 39.3 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.12x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads                   | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                |
| mako                          | 6.99 ms                                                    | 6.37 ms: 1.10x faster                                                 |
| unpickle_pure_python          | 141 us                                                     | 132 us: 1.07x faster                                                  |
| deepcopy_memo                 | 22.6 us                                                    | 21.6 us: 1.05x faster                                                 |
| xml_etree_process             | 37.1 ms                                                    | 35.7 ms: 1.04x faster                                                 |
| pickle_pure_python            | 179 us                                                     | 172 us: 1.04x faster                                                  |
| pathlib                       | 23.3 ms                                                    | 22.5 ms: 1.04x faster                                                 |
| xml_etree_generate            | 52.7 ms                                                    | 51.2 ms: 1.03x faster                                                 |
| float                         | 48.6 ms                                                    | 47.3 ms: 1.03x faster                                                 |
| pyflate                       | 321 ms                                                     | 315 ms: 1.02x faster                                                  |
| xml_etree_iterparse           | 71.5 ms                                                    | 70.2 ms: 1.02x faster                                                 |
| pprint_safe_repr              | 465 ms                                                     | 457 ms: 1.02x faster                                                  |
| fannkuch                      | 248 ms                                                     | 244 ms: 1.02x faster                                                  |
| mdp                           | 1.53 sec                                                   | 1.51 sec: 1.01x faster                                                |
| xml_etree_parse               | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| deepcopy_reduce               | 1.82 us                                                    | 1.81 us: 1.01x faster                                                 |
| pprint_pformat                | 947 ms                                                     | 940 ms: 1.01x faster                                                  |
| json                          | 2.93 ms                                                    | 2.91 ms: 1.01x faster                                                 |
| thrift                        | 435 us                                                     | 433 us: 1.01x faster                                                  |
| json_dumps                    | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                 |
| html5lib                      | 31.2 ms                                                    | 31.0 ms: 1.01x faster                                                 |
| pickle_dict                   | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| pickle                        | 7.48 us                                                    | 7.44 us: 1.01x faster                                                 |
| regex_effbot                  | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                                 |
| richards                      | 31.8 ms                                                    | 31.7 ms: 1.00x faster                                                 |
| telco                         | 4.60 ms                                                    | 4.59 ms: 1.00x faster                                                 |
| logging_simple                | 3.04 us                                                    | 3.05 us: 1.00x slower                                                 |
| unpickle_list                 | 2.88 us                                                    | 2.89 us: 1.00x slower                                                 |
| generators                    | 22.9 ms                                                    | 23.0 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed | 358 ms                                                     | 360 ms: 1.01x slower                                                  |
| json_loads                    | 16.8 us                                                    | 16.9 us: 1.01x slower                                                 |
| sqlite_synth                  | 1.55 us                                                    | 1.56 us: 1.01x slower                                                 |
| gc_traversal                  | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| pickle_list                   | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| coverage                      | 45.0 ms                                                    | 45.5 ms: 1.01x slower                                                 |
| coroutines                    | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                 |
| richards_super                | 35.2 ms                                                    | 35.6 ms: 1.01x slower                                                 |
| logging_format                | 3.31 us                                                    | 3.35 us: 1.01x slower                                                 |
| create_gc_cycles              | 897 us                                                     | 908 us: 1.01x slower                                                  |
| deepcopy                      | 204 us                                                     | 207 us: 1.01x slower                                                  |
| spectral_norm                 | 66.4 ms                                                    | 67.3 ms: 1.01x slower                                                 |
| regex_v8                      | 17.3 ms                                                    | 17.5 ms: 1.01x slower                                                 |
| go                            | 101 ms                                                     | 102 ms: 1.02x slower                                                  |
| unpickle                      | 9.12 us                                                    | 9.27 us: 1.02x slower                                                 |
| scimark_fft                   | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| async_tree_eager_tg           | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                 |
| async_tree_none               | 209 ms                                                     | 216 ms: 1.03x slower                                                  |
| meteor_contest                | 70.3 ms                                                    | 72.5 ms: 1.03x slower                                                 |
| chameleon                     | 4.27 ms                                                    | 4.42 ms: 1.04x slower                                                 |
| scimark_monte_carlo           | 42.5 ms                                                    | 44.3 ms: 1.04x slower                                                 |
| logging_silent                | 60.1 ns                                                    | 62.9 ns: 1.05x slower                                                 |
| sympy_str                     | 131 ms                                                     | 137 ms: 1.05x slower                                                  |
| async_generators              | 281 ms                                                     | 294 ms: 1.05x slower                                                  |
| python_startup                | 15.2 ms                                                    | 15.9 ms: 1.05x slower                                                 |
| docutils                      | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                                |
| sympy_expand                  | 226 ms                                                     | 237 ms: 1.05x slower                                                  |
| crypto_pyaes                  | 49.5 ms                                                    | 52.0 ms: 1.05x slower                                                 |
| scimark_sparse_mat_mult       | 2.77 ms                                                    | 2.92 ms: 1.05x slower                                                 |
| pycparser                     | 632 ms                                                     | 666 ms: 1.05x slower                                                  |
| scimark_sor                   | 94.9 ms                                                    | 100 ms: 1.05x slower                                                  |
| sympy_integrate               | 10.3 ms                                                    | 10.9 ms: 1.06x slower                                                 |
| sympy_sum                     | 69.2 ms                                                    | 73.1 ms: 1.06x slower                                                 |
| regex_compile                 | 68.5 ms                                                    | 72.4 ms: 1.06x slower                                                 |
| bench_mp_pool                 | 47.2 ms                                                    | 49.9 ms: 1.06x slower                                                 |
| async_tree_eager              | 60.3 ms                                                    | 64.0 ms: 1.06x slower                                                 |
| sqlglot_optimize              | 30.9 ms                                                    | 32.9 ms: 1.07x slower                                                 |
| 2to3                          | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| nbody                         | 59.6 ms                                                    | 63.7 ms: 1.07x slower                                                 |
| bench_thread_pool             | 447 us                                                     | 480 us: 1.07x slower                                                  |
| python_startup_no_site        | 12.3 ms                                                    | 13.3 ms: 1.08x slower                                                 |
| typing_runtime_protocols      | 87.6 us                                                    | 95.5 us: 1.09x slower                                                 |
| hexiom                        | 4.06 ms                                                    | 4.43 ms: 1.09x slower                                                 |
| asyncio_tcp                   | 402 ms                                                     | 440 ms: 1.09x slower                                                  |
| nqueens                       | 52.2 ms                                                    | 57.4 ms: 1.10x slower                                                 |
| raytrace                      | 147 ms                                                     | 162 ms: 1.10x slower                                                  |
| django_template               | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                                 |
| sqlglot_transpile             | 891 us                                                     | 1.00 ms: 1.12x slower                                                 |
| sqlglot_parse                 | 732 us                                                     | 826 us: 1.13x slower                                                  |
| deltablue                     | 2.14 ms                                                    | 2.46 ms: 1.15x slower                                                 |
| chaos                         | 34.0 ms                                                    | 39.2 ms: 1.15x slower                                                 |
| scimark_lu                    | 66.9 ms                                                    | 78.1 ms: 1.17x slower                                                 |
| genshi_text                   | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                 |
| comprehensions                | 10.2 us                                                    | 12.3 us: 1.21x slower                                                 |
| genshi_xml                    | 29.9 ms                                                    | 39.3 ms: 1.31x slower                                                 |
| Geometric mean                | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (20): flaskblogging, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, pidigits, regex_dna, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_io, asyncio_tcp_ssl, tornado_http, dask, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_io, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.52x