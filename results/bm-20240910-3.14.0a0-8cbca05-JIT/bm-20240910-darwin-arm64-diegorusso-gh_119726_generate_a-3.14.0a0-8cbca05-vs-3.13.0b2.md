# Results vs. 3.13.0b2

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: darwin-arm64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.09x slower                                                      |
| docutils       | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                                    |
| html5lib       | 31.2 ms                                                    | 32.6 ms: 1.05x slower                                                     |
| tornado_http   | 66.7 ms                                                    | 83.7 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                      | 1.12x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 683 ms: 1.12x faster                                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 707 ms: 1.09x faster                                                      |
| async_tree_io_tg                 | 565 ms                                                     | 534 ms: 1.06x faster                                                      |
| async_tree_none_tg               | 198 ms                                                     | 188 ms: 1.05x faster                                                      |
| async_tree_memoization           | 260 ms                                                     | 248 ms: 1.05x faster                                                      |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                                      |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                      |
| async_tree_eager                 | 60.3 ms                                                    | 64.7 ms: 1.07x slower                                                     |
| async_tree_memoization_tg        | 240 ms                                                     | 259 ms: 1.08x slower                                                      |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                              |

Benchmark hidden because not significant (3): async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                     |
| nbody          | 59.6 ms                                                    | 63.3 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                     |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                     |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                      |
| regex_compile  | 68.5 ms                                                    | 73.9 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                    |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                      |
| xml_etree_process    | 37.1 ms                                                    | 34.8 ms: 1.06x faster                                                     |
| xml_etree_generate   | 52.7 ms                                                    | 51.2 ms: 1.03x faster                                                     |
| pickle               | 7.48 us                                                    | 7.37 us: 1.02x faster                                                     |
| pickle_pure_python   | 179 us                                                     | 177 us: 1.01x faster                                                      |
| pickle_dict          | 18.3 us                                                    | 18.3 us: 1.00x slower                                                     |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.3 ms: 1.01x slower                                                     |
| unpickle             | 9.12 us                                                    | 9.25 us: 1.01x slower                                                     |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                                     |
| json_dumps           | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                     |
| xml_etree_parse      | 106 ms                                                     | 110 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 17.4 ms: 1.15x slower                                                     |
| python_startup_no_site | 12.3 ms                                                    | 14.2 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.15x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                     |
| django_template | 19.4 ms                                                    | 22.6 ms: 1.16x slower                                                     |
| genshi_text     | 13.9 ms                                                    | 16.4 ms: 1.18x slower                                                     |
| genshi_xml      | 29.9 ms                                                    | 40.4 ms: 1.35x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.15x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.2 us: 1.40x faster                                                     |
| deepcopy                         | 204 us                                                     | 155 us: 1.32x faster                                                      |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                     |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                    |
| async_tree_eager_io              | 766 ms                                                     | 683 ms: 1.12x faster                                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 707 ms: 1.09x faster                                                      |
| mako                             | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                     |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                      |
| scimark_sor                      | 94.9 ms                                                    | 88.9 ms: 1.07x faster                                                     |
| xml_etree_process                | 37.1 ms                                                    | 34.8 ms: 1.06x faster                                                     |
| mdp                              | 1.53 sec                                                   | 1.45 sec: 1.06x faster                                                    |
| async_tree_io_tg                 | 565 ms                                                     | 534 ms: 1.06x faster                                                      |
| async_tree_none_tg               | 198 ms                                                     | 188 ms: 1.05x faster                                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                     |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                     |
| async_tree_memoization           | 260 ms                                                     | 248 ms: 1.05x faster                                                      |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                                      |
| float                            | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                     |
| xml_etree_generate               | 52.7 ms                                                    | 51.2 ms: 1.03x faster                                                     |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                      |
| scimark_lu                       | 66.9 ms                                                    | 65.2 ms: 1.03x faster                                                     |
| thrift                           | 435 us                                                     | 428 us: 1.02x faster                                                      |
| pickle                           | 7.48 us                                                    | 7.37 us: 1.02x faster                                                     |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                                     |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                    |
| pickle_pure_python               | 179 us                                                     | 177 us: 1.01x faster                                                      |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                      |
| pickle_dict                      | 18.3 us                                                    | 18.3 us: 1.00x slower                                                     |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                     |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                     |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                     |
| create_gc_cycles                 | 897 us                                                     | 903 us: 1.01x slower                                                      |
| coverage                         | 45.0 ms                                                    | 45.4 ms: 1.01x slower                                                     |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.3 ms: 1.01x slower                                                     |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.09 sec: 1.01x slower                                                    |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                     |
| unpickle                         | 9.12 us                                                    | 9.25 us: 1.01x slower                                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                      |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                                     |
| sqlite_synth                     | 1.55 us                                                    | 1.58 us: 1.02x slower                                                     |
| json_dumps                       | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                     |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                     |
| spectral_norm                    | 66.4 ms                                                    | 68.1 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                                      |
| pyflate                          | 321 ms                                                     | 331 ms: 1.03x slower                                                      |
| telco                            | 4.60 ms                                                    | 4.76 ms: 1.03x slower                                                     |
| logging_silent                   | 60.1 ns                                                    | 62.5 ns: 1.04x slower                                                     |
| pathlib                          | 23.3 ms                                                    | 24.2 ms: 1.04x slower                                                     |
| xml_etree_parse                  | 106 ms                                                     | 110 ms: 1.04x slower                                                      |
| dulwich_log                      | 27.6 ms                                                    | 28.8 ms: 1.04x slower                                                     |
| html5lib                         | 31.2 ms                                                    | 32.6 ms: 1.05x slower                                                     |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                                     |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                      |
| scimark_fft                      | 181 ms                                                     | 191 ms: 1.06x slower                                                      |
| meteor_contest                   | 70.3 ms                                                    | 74.6 ms: 1.06x slower                                                     |
| nbody                            | 59.6 ms                                                    | 63.3 ms: 1.06x slower                                                     |
| generators                       | 22.9 ms                                                    | 24.4 ms: 1.07x slower                                                     |
| bench_thread_pool                | 447 us                                                     | 477 us: 1.07x slower                                                      |
| pycparser                        | 632 ms                                                     | 677 ms: 1.07x slower                                                      |
| async_tree_eager                 | 60.3 ms                                                    | 64.7 ms: 1.07x slower                                                     |
| typing_runtime_protocols         | 87.6 us                                                    | 94.0 us: 1.07x slower                                                     |
| fannkuch                         | 248 ms                                                     | 267 ms: 1.08x slower                                                      |
| regex_compile                    | 68.5 ms                                                    | 73.9 ms: 1.08x slower                                                     |
| async_tree_memoization_tg        | 240 ms                                                     | 259 ms: 1.08x slower                                                      |
| pprint_safe_repr                 | 465 ms                                                     | 503 ms: 1.08x slower                                                      |
| pprint_pformat                   | 947 ms                                                     | 1.03 sec: 1.09x slower                                                    |
| docutils                         | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                                    |
| 2to3                             | 161 ms                                                     | 176 ms: 1.09x slower                                                      |
| sympy_str                        | 131 ms                                                     | 144 ms: 1.09x slower                                                      |
| sympy_sum                        | 69.2 ms                                                    | 76.0 ms: 1.10x slower                                                     |
| deltablue                        | 2.14 ms                                                    | 2.35 ms: 1.10x slower                                                     |
| sqlglot_normalize                | 166 ms                                                     | 183 ms: 1.10x slower                                                      |
| sympy_expand                     | 226 ms                                                     | 249 ms: 1.10x slower                                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 52.2 ms: 1.11x slower                                                     |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.07 ms: 1.11x slower                                                     |
| nqueens                          | 52.2 ms                                                    | 58.3 ms: 1.12x slower                                                     |
| sympy_integrate                  | 10.3 ms                                                    | 11.6 ms: 1.12x slower                                                     |
| scimark_monte_carlo              | 42.5 ms                                                    | 48.6 ms: 1.14x slower                                                     |
| python_startup                   | 15.2 ms                                                    | 17.4 ms: 1.15x slower                                                     |
| sqlglot_optimize                 | 30.9 ms                                                    | 35.5 ms: 1.15x slower                                                     |
| python_startup_no_site           | 12.3 ms                                                    | 14.2 ms: 1.15x slower                                                     |
| hexiom                           | 4.06 ms                                                    | 4.71 ms: 1.16x slower                                                     |
| django_template                  | 19.4 ms                                                    | 22.6 ms: 1.16x slower                                                     |
| sqlglot_transpile                | 891 us                                                     | 1.04 ms: 1.17x slower                                                     |
| sqlglot_parse                    | 732 us                                                     | 858 us: 1.17x slower                                                      |
| genshi_text                      | 13.9 ms                                                    | 16.4 ms: 1.18x slower                                                     |
| raytrace                         | 147 ms                                                     | 174 ms: 1.18x slower                                                      |
| chaos                            | 34.0 ms                                                    | 40.3 ms: 1.19x slower                                                     |
| pylint                           | 170 ms                                                     | 206 ms: 1.21x slower                                                      |
| tornado_http                     | 66.7 ms                                                    | 83.7 ms: 1.26x slower                                                     |
| comprehensions                   | 10.2 us                                                    | 12.8 us: 1.26x slower                                                     |
| richards_super                   | 35.2 ms                                                    | 46.8 ms: 1.33x slower                                                     |
| genshi_xml                       | 29.9 ms                                                    | 40.4 ms: 1.35x slower                                                     |
| richards                         | 31.8 ms                                                    | 45.0 ms: 1.41x slower                                                     |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                              |

Benchmark hidden because not significant (8): async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, pickle_list, logging_format, pidigits, go, async_tree_eager_memoization, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.51x