# Results vs. 3.13.0b2

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: darwin-arm64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.01x faster
- HPT reliability: 92.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 159 ms: 1.01x faster                                                     |
| docutils       | 1.44 sec                                                   | 1.46 sec: 1.02x slower                                                   |
| tornado_http   | 66.7 ms                                                    | 84.9 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                      | 1.06x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                     |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                     |
| async_tree_eager_io_tg           | 768 ms                                                     | 713 ms: 1.08x faster                                                     |
| async_tree_memoization           | 260 ms                                                     | 249 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                     |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                    |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                     |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                     |
| async_tree_io                    | 563 ms                                                     | 593 ms: 1.05x slower                                                     |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (6): async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                    |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x faster                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                    |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                    |
| regex_compile  | 68.5 ms                                                    | 66.7 ms: 1.03x faster                                                    |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 52.4 ms: 1.01x faster                                                    |
| tomli_loads          | 1.47 sec                                                   | 1.47 sec: 1.01x slower                                                   |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                     |
| json_dumps           | 6.23 ms                                                    | 6.33 ms: 1.02x slower                                                    |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                     |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                    |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                     |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                                    |
| python_startup_no_site | 12.3 ms                                                    | 12.5 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                    |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                    |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.01x slower                                                    |
| mako            | 6.99 ms                                                    | 7.09 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.41x faster                                                     |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.33x faster                                                    |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                    |
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                     |
| generators                       | 22.9 ms                                                    | 20.5 ms: 1.12x faster                                                    |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                     |
| async_tree_eager_io_tg           | 768 ms                                                     | 713 ms: 1.08x faster                                                     |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                   |
| richards_super                   | 35.2 ms                                                    | 33.0 ms: 1.07x faster                                                    |
| richards                         | 31.8 ms                                                    | 30.3 ms: 1.05x faster                                                    |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                    |
| async_tree_memoization           | 260 ms                                                     | 249 ms: 1.04x faster                                                     |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                    |
| thrift                           | 435 us                                                     | 420 us: 1.04x faster                                                     |
| pprint_safe_repr                 | 465 ms                                                     | 449 ms: 1.03x faster                                                     |
| regex_compile                    | 68.5 ms                                                    | 66.7 ms: 1.03x faster                                                    |
| pprint_pformat                   | 947 ms                                                     | 923 ms: 1.03x faster                                                     |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                     |
| dulwich_log                      | 27.6 ms                                                    | 27.0 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                     |
| comprehensions                   | 10.2 us                                                    | 9.99 us: 1.02x faster                                                    |
| 2to3                             | 161 ms                                                     | 159 ms: 1.01x faster                                                     |
| scimark_sor                      | 94.9 ms                                                    | 93.6 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                   |
| coverage                         | 45.0 ms                                                    | 44.6 ms: 1.01x faster                                                    |
| xml_etree_generate               | 52.7 ms                                                    | 52.4 ms: 1.01x faster                                                    |
| genshi_text                      | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                    |
| sympy_sum                        | 69.2 ms                                                    | 68.9 ms: 1.00x faster                                                    |
| deltablue                        | 2.14 ms                                                    | 2.13 ms: 1.00x faster                                                    |
| nbody                            | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                    |
| create_gc_cycles                 | 897 us                                                     | 894 us: 1.00x faster                                                     |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                     |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                     |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.78 ms: 1.00x slower                                                    |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                    |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                    |
| bench_thread_pool                | 447 us                                                     | 449 us: 1.01x slower                                                     |
| sqlglot_transpile                | 891 us                                                     | 896 us: 1.01x slower                                                     |
| tomli_loads                      | 1.47 sec                                                   | 1.47 sec: 1.01x slower                                                   |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.01x slower                                                     |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                    |
| python_startup                   | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                                    |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                                     |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                    |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                                     |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                     |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                    |
| sqlglot_normalize                | 166 ms                                                     | 168 ms: 1.01x slower                                                     |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                    |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                     |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                    |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                    |
| logging_silent                   | 60.1 ns                                                    | 60.9 ns: 1.01x slower                                                    |
| sqlglot_parse                    | 732 us                                                     | 742 us: 1.01x slower                                                     |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.01x slower                                                    |
| mako                             | 6.99 ms                                                    | 7.09 ms: 1.02x slower                                                    |
| json_dumps                       | 6.23 ms                                                    | 6.33 ms: 1.02x slower                                                    |
| docutils                         | 1.44 sec                                                   | 1.46 sec: 1.02x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                     |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                    |
| python_startup_no_site           | 12.3 ms                                                    | 12.5 ms: 1.02x slower                                                    |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                    |
| crypto_pyaes                     | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                                    |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                     |
| bench_mp_pool                    | 47.2 ms                                                    | 48.2 ms: 1.02x slower                                                    |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                     |
| nqueens                          | 52.2 ms                                                    | 53.5 ms: 1.02x slower                                                    |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                    |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.03x slower                                                    |
| meteor_contest                   | 70.3 ms                                                    | 72.1 ms: 1.03x slower                                                    |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.03x slower                                                   |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                     |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                    |
| typing_runtime_protocols         | 87.6 us                                                    | 90.3 us: 1.03x slower                                                    |
| go                               | 101 ms                                                     | 104 ms: 1.04x slower                                                     |
| telco                            | 4.60 ms                                                    | 4.79 ms: 1.04x slower                                                    |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                    |
| async_tree_io                    | 563 ms                                                     | 593 ms: 1.05x slower                                                     |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.06x slower                                                     |
| tornado_http                     | 66.7 ms                                                    | 84.9 ms: 1.27x slower                                                    |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (17): async_tree_eager_memoization_tg, async_tree_none_tg, scimark_lu, async_generators, xml_etree_process, async_tree_io_tg, hexiom, sympy_integrate, pyflate, html5lib, float, json, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 92.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.42x