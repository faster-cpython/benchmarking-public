# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.00x faster
- HPT reliability: 95.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 162 ms: 1.01x slower                                         |
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                       |
| html5lib       | 31.2 ms                                                    | 30.2 ms: 1.03x faster                                        |
| tornado_http   | 66.7 ms                                                    | 82.2 ms: 1.23x slower                                        |
| Geometric mean | (ref)                                                      | 1.05x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 678 ms: 1.13x faster                                         |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                         |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                         |
| async_tree_none_tg               | 198 ms                                                     | 189 ms: 1.05x faster                                         |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                         |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                         |
| async_tree_eager                 | 60.3 ms                                                    | 60.5 ms: 1.00x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                         |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.02x slower                                         |
| async_tree_io                    | 563 ms                                                     | 583 ms: 1.04x slower                                         |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                         |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                 |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.9 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                        |
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                        |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                         |
| regex_compile  | 68.5 ms                                                    | 67.4 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                      | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.40 us: 1.01x faster                                        |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.01x faster                                         |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                        |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                       |
| unpickle_list        | 2.88 us                                                    | 2.92 us: 1.01x slower                                        |
| xml_etree_process    | 37.1 ms                                                    | 37.6 ms: 1.01x slower                                        |
| xml_etree_generate   | 52.7 ms                                                    | 53.5 ms: 1.02x slower                                        |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                        |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.6 ms: 1.03x slower                                        |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                         |
| pickle_pure_python   | 179 us                                                     | 184 us: 1.03x slower                                         |
| unpickle             | 9.12 us                                                    | 9.43 us: 1.03x slower                                        |
| json_dumps           | 6.23 ms                                                    | 6.46 ms: 1.04x slower                                        |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                 |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.5 ms: 1.09x slower                                        |
| python_startup_no_site | 12.3 ms                                                    | 13.6 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                      | 1.09x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                        |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                 |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                         |
| deepcopy_memo                    | 22.6 us                                                    | 16.4 us: 1.37x faster                                        |
| go                               | 101 ms                                                     | 79.3 ms: 1.27x faster                                        |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                        |
| async_tree_eager_io              | 766 ms                                                     | 678 ms: 1.13x faster                                         |
| generators                       | 22.9 ms                                                    | 20.8 ms: 1.10x faster                                        |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                         |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.07x faster                                       |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                         |
| regex_v8                         | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                        |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                        |
| async_tree_none_tg               | 198 ms                                                     | 189 ms: 1.05x faster                                         |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                         |
| html5lib                         | 31.2 ms                                                    | 30.2 ms: 1.03x faster                                        |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                         |
| thrift                           | 435 us                                                     | 425 us: 1.02x faster                                         |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                         |
| pprint_safe_repr                 | 465 ms                                                     | 456 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                         |
| regex_compile                    | 68.5 ms                                                    | 67.4 ms: 1.02x faster                                        |
| pprint_pformat                   | 947 ms                                                     | 932 ms: 1.02x faster                                         |
| scimark_sor                      | 94.9 ms                                                    | 93.5 ms: 1.01x faster                                        |
| pickle                           | 7.48 us                                                    | 7.40 us: 1.01x faster                                        |
| create_gc_cycles                 | 897 us                                                     | 888 us: 1.01x faster                                         |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                        |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.01x faster                                         |
| docutils                         | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                       |
| comprehensions                   | 10.2 us                                                    | 10.1 us: 1.01x faster                                        |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                       |
| logging_simple                   | 3.04 us                                                    | 3.03 us: 1.01x faster                                        |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                         |
| hexiom                           | 4.06 ms                                                    | 4.05 ms: 1.00x faster                                        |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                         |
| async_tree_eager                 | 60.3 ms                                                    | 60.5 ms: 1.00x slower                                        |
| sqlite_synth                     | 1.55 us                                                    | 1.56 us: 1.00x slower                                        |
| logging_format                   | 3.31 us                                                    | 3.32 us: 1.00x slower                                        |
| sympy_str                        | 131 ms                                                     | 132 ms: 1.00x slower                                         |
| float                            | 48.6 ms                                                    | 48.9 ms: 1.01x slower                                        |
| bench_thread_pool                | 447 us                                                     | 450 us: 1.01x slower                                         |
| 2to3                             | 161 ms                                                     | 162 ms: 1.01x slower                                         |
| logging_silent                   | 60.1 ns                                                    | 60.6 ns: 1.01x slower                                        |
| pycparser                        | 632 ms                                                     | 638 ms: 1.01x slower                                         |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                         |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                        |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                         |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                       |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                        |
| sqlglot_parse                    | 732 us                                                     | 741 us: 1.01x slower                                         |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                         |
| json                             | 2.93 ms                                                    | 2.97 ms: 1.01x slower                                        |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                        |
| unpickle_list                    | 2.88 us                                                    | 2.92 us: 1.01x slower                                        |
| xml_etree_process                | 37.1 ms                                                    | 37.6 ms: 1.01x slower                                        |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.1 ms: 1.01x slower                                        |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.81 ms: 1.01x slower                                        |
| xml_etree_generate               | 52.7 ms                                                    | 53.5 ms: 1.02x slower                                        |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                        |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                        |
| richards                         | 31.8 ms                                                    | 32.3 ms: 1.02x slower                                        |
| raytrace                         | 147 ms                                                     | 149 ms: 1.02x slower                                         |
| crypto_pyaes                     | 49.5 ms                                                    | 50.3 ms: 1.02x slower                                        |
| spectral_norm                    | 66.4 ms                                                    | 67.5 ms: 1.02x slower                                        |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                        |
| sqlglot_transpile                | 891 us                                                     | 908 us: 1.02x slower                                         |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                        |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                         |
| richards_super                   | 35.2 ms                                                    | 36.0 ms: 1.02x slower                                        |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.02x slower                                         |
| nqueens                          | 52.2 ms                                                    | 53.6 ms: 1.03x slower                                        |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.14 sec: 1.03x slower                                       |
| bench_mp_pool                    | 47.2 ms                                                    | 48.5 ms: 1.03x slower                                        |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.6 ms: 1.03x slower                                        |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                         |
| pickle_pure_python               | 179 us                                                     | 184 us: 1.03x slower                                         |
| typing_runtime_protocols         | 87.6 us                                                    | 90.4 us: 1.03x slower                                        |
| unpickle                         | 9.12 us                                                    | 9.43 us: 1.03x slower                                        |
| async_tree_io                    | 563 ms                                                     | 583 ms: 1.04x slower                                         |
| json_dumps                       | 6.23 ms                                                    | 6.46 ms: 1.04x slower                                        |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                         |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                        |
| telco                            | 4.60 ms                                                    | 4.87 ms: 1.06x slower                                        |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                         |
| python_startup                   | 15.2 ms                                                    | 16.5 ms: 1.09x slower                                        |
| python_startup_no_site           | 12.3 ms                                                    | 13.6 ms: 1.10x slower                                        |
| tornado_http                     | 66.7 ms                                                    | 82.2 ms: 1.23x slower                                        |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                 |

Benchmark hidden because not significant (17): async_tree_io_tg, mako, sympy_sum, coverage, sympy_integrate, deltablue, gc_traversal, nbody, async_tree_eager_memoization, pidigits, pickle_dict, scimark_lu, async_generators, genshi_text, async_tree_eager_cpu_io_mixed, asyncio_tcp, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035.json: unpack_sequence

# HPT report

- Reliability score: 95.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.48x