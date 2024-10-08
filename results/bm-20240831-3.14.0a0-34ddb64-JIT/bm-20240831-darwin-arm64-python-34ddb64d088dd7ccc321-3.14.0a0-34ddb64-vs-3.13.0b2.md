# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.73x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 180 ms: 1.12x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.61 sec: 1.12x slower                                                |
| html5lib       | 31.2 ms                                                    | 32.8 ms: 1.05x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 87.9 ms: 1.32x slower                                                 |
| Geometric mean | (ref)                                                      | 1.15x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.13x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 718 ms: 1.07x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 463 ms: 1.03x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 160 ms: 1.05x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.3 ms: 1.05x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 594 ms: 1.05x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.4 ms: 1.05x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 63.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.04x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 74.9 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 34.6 ms: 1.07x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 133 us: 1.06x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 50.7 ms: 1.04x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 177 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 71.9 ms: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.28 ms: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.8 ms: 1.11x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                 |
| django_template | 19.4 ms                                                    | 22.1 ms: 1.14x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.8 ms: 1.21x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 41.2 ms: 1.38x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.1 us: 1.40x faster                                                 |
| deepcopy                         | 204 us                                                     | 154 us: 1.32x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.49 us: 1.22x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.13x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 34.6 ms: 1.07x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 718 ms: 1.07x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 88.7 ms: 1.07x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 133 us: 1.06x faster                                                  |
| float                            | 48.6 ms                                                    | 46.4 ms: 1.05x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.04x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 50.7 ms: 1.04x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| thrift                           | 435 us                                                     | 427 us: 1.02x faster                                                  |
| scimark_lu                       | 66.9 ms                                                    | 65.7 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                                  |
| pickle_pure_python               | 179 us                                                     | 177 us: 1.01x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| logging_simple                   | 3.04 us                                                    | 3.03 us: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.2 ms: 1.00x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 71.9 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.28 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 904 us: 1.01x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.34 us: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| go                               | 101 ms                                                     | 102 ms: 1.01x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.10 sec: 1.01x slower                                                |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                  |
| mdp                              | 1.53 sec                                                   | 1.57 sec: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                                  |
| pyflate                          | 321 ms                                                     | 328 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 463 ms: 1.03x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 68.3 ms: 1.03x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 62.4 ns: 1.04x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 160 ms: 1.05x slower                                                  |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.3 ms: 1.05x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 73.8 ms: 1.05x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 32.8 ms: 1.05x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.85 ms: 1.05x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 52.1 ms: 1.05x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 594 ms: 1.05x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 29.1 ms: 1.06x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 191 ms: 1.06x slower                                                  |
| fannkuch                         | 248 ms                                                     | 264 ms: 1.06x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 474 us: 1.06x slower                                                  |
| nbody                            | 59.6 ms                                                    | 63.8 ms: 1.07x slower                                                 |
| generators                       | 22.9 ms                                                    | 24.6 ms: 1.07x slower                                                 |
| pycparser                        | 632 ms                                                     | 681 ms: 1.08x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 95.0 us: 1.09x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 74.9 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 51.6 ms: 1.09x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 1.04 sec: 1.10x slower                                                |
| asyncio_tcp                      | 402 ms                                                     | 442 ms: 1.10x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 511 ms: 1.10x slower                                                  |
| sympy_str                        | 131 ms                                                     | 145 ms: 1.10x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 76.4 ms: 1.10x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.07 ms: 1.11x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 250 ms: 1.11x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.8 ms: 1.11x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 184 ms: 1.11x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.39 ms: 1.12x slower                                                 |
| 2to3                             | 161 ms                                                     | 180 ms: 1.12x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.61 sec: 1.12x slower                                                |
| python_startup_no_site           | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                                 |
| django_template                  | 19.4 ms                                                    | 22.1 ms: 1.14x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 59.5 ms: 1.14x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 48.6 ms: 1.15x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 11.9 ms: 1.15x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 857 us: 1.17x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 36.2 ms: 1.17x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.05 ms: 1.18x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.78 ms: 1.18x slower                                                 |
| raytrace                         | 147 ms                                                     | 174 ms: 1.18x slower                                                  |
| chaos                            | 34.0 ms                                                    | 40.4 ms: 1.19x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.8 ms: 1.21x slower                                                 |
| pylint                           | 170 ms                                                     | 207 ms: 1.22x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 12.8 us: 1.26x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 87.9 ms: 1.32x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 41.2 ms: 1.38x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 49.7 ms: 1.41x slower                                                 |
| richards                         | 31.8 ms                                                    | 47.7 ms: 1.50x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_eager_memoization_tg, asyncio_websockets, json, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.73x