# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.00x faster
- HPT reliability: 98.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 162 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.1 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 83.1 ms: 1.25x slower                                                 |
| Geometric mean | (ref)                                                      | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.12x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.09x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 717 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 595 ms: 1.06x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_eager_memoization_tg, async_tree_eager, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 48.7 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.04x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 147 ms: 1.02x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 183 us: 1.03x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.43 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.04x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.1 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.6 ms: 1.09x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.94 ms: 1.01x faster                                                 |
| django_template | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.5 us: 1.37x faster                                                 |
| go                               | 101 ms                                                     | 79.2 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.12x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.09x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.07x faster                                                |
| async_tree_eager_io_tg           | 768 ms                                                     | 717 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.04x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.04x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.1 ms: 1.04x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 450 ms: 1.03x faster                                                  |
| thrift                           | 435 us                                                     | 422 us: 1.03x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 922 ms: 1.03x faster                                                  |
| dulwich_log                      | 27.6 ms                                                    | 27.0 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| comprehensions                   | 10.2 us                                                    | 9.96 us: 1.02x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 93.1 ms: 1.02x faster                                                 |
| regex_dna                        | 149 ms                                                     | 147 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                                |
| richards                         | 31.8 ms                                                    | 31.4 ms: 1.01x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 67.8 ms: 1.01x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.94 ms: 1.01x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 35.1 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| hexiom                           | 4.06 ms                                                    | 4.07 ms: 1.00x slower                                                 |
| float                            | 48.6 ms                                                    | 48.7 ms: 1.00x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.00x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.79 ms: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 451 us: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 905 us: 1.01x slower                                                  |
| json                             | 2.93 ms                                                    | 2.96 ms: 1.01x slower                                                 |
| 2to3                             | 161 ms                                                     | 162 ms: 1.01x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 902 us: 1.01x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 741 us: 1.01x slower                                                  |
| pycparser                        | 632 ms                                                     | 641 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.09 us: 1.02x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.5 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 61.3 ns: 1.02x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.6 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 53.6 ms: 1.03x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 183 us: 1.03x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.14 sec: 1.03x slower                                                |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 24.0 ms: 1.03x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.4 ms: 1.03x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.41 us: 1.03x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.43 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.9 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.04x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.1 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.6 us: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.84 ms: 1.05x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 595 ms: 1.06x slower                                                  |
| fannkuch                         | 248 ms                                                     | 263 ms: 1.06x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.8 ms: 1.06x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.6 ms: 1.09x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 83.1 ms: 1.25x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (21): async_tree_memoization, async_tree_eager_memoization_tg, scimark_lu, sympy_sum, nbody, async_generators, genshi_text, sympy_integrate, asyncio_websockets, sympy_str, pyflate, async_tree_eager, coverage, tomli_loads, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_eager_memoization, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.60x