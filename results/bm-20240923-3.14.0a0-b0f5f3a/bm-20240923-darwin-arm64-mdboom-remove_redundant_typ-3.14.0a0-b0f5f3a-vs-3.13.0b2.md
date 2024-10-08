# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_redundant_typ
- machine: darwin-arm64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.01x faster
- HPT reliability: 53.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 85.8 ms: 1.29x slower                                                 |
| Geometric mean | (ref)                                                      | 1.06x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.05x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.8 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 460 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 60.0 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.0 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.34 us: 1.02x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.00x faster                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.47 sec: 1.00x slower                                                |
| xml_etree_generate   | 52.7 ms                                                    | 52.9 ms: 1.00x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 180 us: 1.01x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.30 ms: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (3): unpickle, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.0 ms: 1.06x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.1 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| mako            | 6.99 ms                                                    | 7.12 ms: 1.02x slower                                                 |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.6 us: 1.36x faster                                                 |
| go                               | 101 ms                                                     | 79.2 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.22x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.09x faster                                                  |
| generators                       | 22.9 ms                                                    | 21.1 ms: 1.08x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 64.6 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.70 ms: 1.03x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 67.0 ms: 1.02x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 92.7 ms: 1.02x faster                                                 |
| thrift                           | 435 us                                                     | 426 us: 1.02x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 930 ms: 1.02x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.34 us: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 457 ms: 1.02x faster                                                  |
| logging_simple                   | 3.04 us                                                    | 3.00 us: 1.01x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.4 ms: 1.01x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                                 |
| scimark_fft                      | 181 ms                                                     | 179 ms: 1.01x faster                                                  |
| logging_format                   | 3.31 us                                                    | 3.28 us: 1.01x faster                                                 |
| async_generators                 | 281 ms                                                     | 278 ms: 1.01x faster                                                  |
| json                             | 2.93 ms                                                    | 2.91 ms: 1.01x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                                 |
| genshi_text                      | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                 |
| sympy_sum                        | 69.2 ms                                                    | 68.7 ms: 1.01x faster                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| create_gc_cycles                 | 897 us                                                     | 892 us: 1.01x faster                                                  |
| spectral_norm                    | 66.4 ms                                                    | 66.0 ms: 1.01x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.13 ms: 1.00x faster                                                 |
| hexiom                           | 4.06 ms                                                    | 4.04 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.4 ms: 1.00x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.45 ms: 1.00x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.47 sec: 1.00x slower                                                |
| xml_etree_generate               | 52.7 ms                                                    | 52.9 ms: 1.00x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 736 us: 1.01x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.1 ms: 1.01x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.01x slower                                                  |
| nbody                            | 59.6 ms                                                    | 60.0 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| pickle_pure_python               | 179 us                                                     | 180 us: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.8 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 898 us: 1.01x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 50.0 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.30 ms: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 60.8 ns: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.3 ms: 1.01x slower                                                 |
| raytrace                         | 147 ms                                                     | 149 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 48.0 ms: 1.02x slower                                                 |
| richards                         | 31.8 ms                                                    | 32.4 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.2 ms: 1.02x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.12 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 460 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.02x slower                                                |
| richards_super                   | 35.2 ms                                                    | 36.2 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.81 ms: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.6 ms: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 261 ms: 1.05x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.0 ms: 1.06x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.1 ms: 1.06x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 93.6 us: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.07x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 85.8 ms: 1.29x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (16): async_tree_io_tg, asyncio_tcp_ssl, unpickle, async_tree_eager_memoization, pyflate, float, json_loads, bench_thread_pool, async_tree_eager_cpu_io_mixed, pickle_list, sympy_str, 2to3, pathlib, pycparser, asyncio_tcp, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: unpack_sequence

# HPT report

- Reliability score: 53.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.42x