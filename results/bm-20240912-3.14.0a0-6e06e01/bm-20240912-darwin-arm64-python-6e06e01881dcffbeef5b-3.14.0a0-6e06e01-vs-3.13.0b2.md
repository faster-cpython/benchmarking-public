# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: darwin-arm64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 75.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.00x faster                                                |
| html5lib       | 31.2 ms                                                    | 30.2 ms: 1.03x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 85.1 ms: 1.28x slower                                                 |
| Geometric mean | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 678 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 706 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 187 ms: 1.06x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 122 ms: 1.02x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 579 ms: 1.03x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 49.3 ms: 1.02x slower                                                 |
| nbody          | 59.6 ms                                                    | 60.9 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 66.9 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 141 us                                                     | 141 us: 1.00x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.21 us: 1.01x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                  |
| unpickle_list        | 2.88 us                                                    | 2.94 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.39 ms: 1.03x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.2 ms: 1.04x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (3): pickle_list, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.89 ms: 1.01x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.41x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.5 us: 1.37x faster                                                 |
| go                               | 101 ms                                                     | 79.0 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 678 ms: 1.13x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 706 ms: 1.09x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 187 ms: 1.06x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.04x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.2 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 452 ms: 1.03x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 66.9 ms: 1.03x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 122 ms: 1.02x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 924 ms: 1.02x faster                                                  |
| thrift                           | 435 us                                                     | 426 us: 1.02x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 93.0 ms: 1.02x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 22.9 ms: 1.02x faster                                                 |
| comprehensions                   | 10.2 us                                                    | 9.99 us: 1.02x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.2 ms: 1.02x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.89 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.5 ms: 1.01x faster                                                 |
| sympy_sum                        | 69.2 ms                                                    | 68.5 ms: 1.01x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.6 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                                 |
| docutils                         | 1.44 sec                                                   | 1.43 sec: 1.00x faster                                                |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 141 us: 1.00x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 35.4 ms: 1.00x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.06 us: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 450 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.79 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.21 us: 1.01x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 67.6 ms: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 60.8 ns: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.10 ms: 1.01x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.36 us: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                                 |
| float                            | 48.6 ms                                                    | 49.3 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 905 us: 1.02x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 744 us: 1.02x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.1 ms: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 2.94 us: 1.02x slower                                                 |
| raytrace                         | 147 ms                                                     | 150 ms: 1.02x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                                 |
| nbody                            | 59.6 ms                                                    | 60.9 ms: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.0 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.02x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 68.0 ms: 1.03x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.03x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.03x slower                                                |
| json_dumps                       | 6.23 ms                                                    | 6.39 ms: 1.03x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.6 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 579 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.2 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.5 us: 1.05x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.82 ms: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.8 ms: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 261 ms: 1.05x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.9 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 85.1 ms: 1.28x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (24): async_tree_io_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, 2to3, async_generators, sympy_str, python_startup, async_tree_eager_cpu_io_mixed, async_tree_eager, pidigits, deltablue, asyncio_websockets, pickle_list, gc_traversal, pickle, create_gc_cycles, sympy_expand, sqlite_synth, pickle_dict, pyflate, json, python_startup_no_site, asyncio_tcp, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: unpack_sequence

# HPT report

- Reliability score: 75.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.51x