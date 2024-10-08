# Results vs. 3.13.0b2

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: darwin-arm64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.00x faster
- HPT reliability: 90.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 158 ms: 1.02x faster                                                  |
| docutils       | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 84.9 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 685 ms: 1.12x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 716 ms: 1.07x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.6 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 594 ms: 1.05x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (6): async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.43 sec: 1.03x faster                                                |
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 184 us: 1.03x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.42 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.9 ms: 1.05x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.91 ms: 1.01x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.33x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 685 ms: 1.12x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.8 ms: 1.10x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 716 ms: 1.07x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.07x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| thrift                           | 435 us                                                     | 419 us: 1.04x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.43 sec: 1.03x faster                                                |
| dulwich_log                      | 27.6 ms                                                    | 26.9 ms: 1.02x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.1 ms: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 454 ms: 1.02x faster                                                  |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 93.0 ms: 1.02x faster                                                 |
| 2to3                             | 161 ms                                                     | 158 ms: 1.02x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 931 ms: 1.02x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.91 ms: 1.01x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.12 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.8 ms: 1.01x faster                                                 |
| pyflate                          | 321 ms                                                     | 319 ms: 1.00x faster                                                  |
| async_generators                 | 281 ms                                                     | 280 ms: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.78 ms: 1.00x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 449 us: 1.00x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                 |
| sympy_str                        | 131 ms                                                     | 132 ms: 1.00x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 901 us: 1.00x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.01x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.06 us: 1.01x slower                                                 |
| nbody                            | 59.6 ms                                                    | 60.1 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 900 us: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 67.1 ms: 1.01x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 61.1 ns: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 745 us: 1.02x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.3 us: 1.02x slower                                                 |
| pycparser                        | 632 ms                                                     | 644 ms: 1.02x slower                                                  |
| raytrace                         | 147 ms                                                     | 150 ms: 1.02x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.37 us: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.2 ms: 1.02x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| telco                            | 4.60 ms                                                    | 4.69 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 72.1 ms: 1.03x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.03x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.03x slower                                                |
| chaos                            | 34.0 ms                                                    | 34.9 ms: 1.03x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.8 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 48.6 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 184 us: 1.03x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.6 ms: 1.03x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.42 ms: 1.03x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.4 us: 1.04x slower                                                 |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 15.9 ms: 1.05x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 594 ms: 1.05x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                                 |
| go                               | 101 ms                                                     | 108 ms: 1.07x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 84.9 ms: 1.27x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (15): sympy_sum, asyncio_tcp, async_tree_eager_memoization_tg, scimark_lu, pidigits, json, float, hexiom, pathlib, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 90.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.60x