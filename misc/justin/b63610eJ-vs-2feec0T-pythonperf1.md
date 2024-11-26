Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 218 ms                                                                      | 219 ms: 1.01x slower                                                |
| chameleon      | 4.93 ms                                                                     | 4.86 ms: 1.01x faster                                               |
| docutils       | 1.59 sec                                                                    | 1.59 sec: 1.00x slower                                              |
| tornado_http   | 88.0 ms                                                                     | 89.4 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 268 ms                                                                      | 263 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 456 ms                                                                      | 449 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                      | 464 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                        |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 82.3 ms                                                                     | 61.9 ms: 1.33x faster                                               |
| float          | 57.1 ms                                                                     | 51.4 ms: 1.11x faster                                               |
| pidigits       | 151 ms                                                                      | 152 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                       | 1.13x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 84.4 ms                                                                     | 83.8 ms: 1.01x faster                                               |
| regex_dna      | 121 ms                                                                      | 122 ms: 1.01x slower                                                |
| regex_effbot   | 1.57 ms                                                                     | 1.60 ms: 1.02x slower                                               |
| regex_v8       | 15.1 ms                                                                     | 15.5 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.39 us                                                                     | 2.77 us: 1.22x faster                                               |
| tomli_loads          | 1.47 sec                                                                    | 1.32 sec: 1.11x faster                                              |
| pickle_dict          | 18.7 us                                                                     | 17.6 us: 1.06x faster                                               |
| xml_etree_iterparse  | 67.0 ms                                                                     | 63.7 ms: 1.05x faster                                               |
| xml_etree_generate   | 54.8 ms                                                                     | 52.8 ms: 1.04x faster                                               |
| xml_etree_process    | 37.1 ms                                                                     | 36.2 ms: 1.02x faster                                               |
| unpickle_pure_python | 135 us                                                                      | 133 us: 1.02x faster                                                |
| xml_etree_parse      | 94.2 ms                                                                     | 92.8 ms: 1.02x faster                                               |
| pickle_pure_python   | 181 us                                                                      | 179 us: 1.01x faster                                                |
| json_loads           | 13.3 us                                                                     | 13.4 us: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                       | 1.04x faster                                                        |

Benchmark hidden because not significant (4): unpickle, unpickle_list, json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                                     | 21.0 ms: 1.04x slower                                               |
| python_startup_no_site | 18.1 ms                                                                     | 19.1 ms: 1.05x slower                                               |
| Geometric mean         | (ref)                                                                       | 1.05x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 6.96 ms                                                                     | 6.59 ms: 1.06x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231218-pythonperf1-amd64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf1-amd64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody                      | 82.3 ms                                                                     | 61.9 ms: 1.33x faster                                               |
| spectral_norm              | 82.6 ms                                                                     | 66.4 ms: 1.24x faster                                               |
| deltablue                  | 2.67 ms                                                                     | 2.14 ms: 1.24x faster                                               |
| pickle_list                | 3.39 us                                                                     | 2.77 us: 1.22x faster                                               |
| fannkuch                   | 291 ms                                                                      | 249 ms: 1.17x faster                                                |
| float                      | 57.1 ms                                                                     | 51.4 ms: 1.11x faster                                               |
| scimark_sparse_mat_mult    | 2.98 ms                                                                     | 2.68 ms: 1.11x faster                                               |
| tomli_loads                | 1.47 sec                                                                    | 1.32 sec: 1.11x faster                                              |
| comprehensions             | 12.8 us                                                                     | 11.6 us: 1.11x faster                                               |
| scimark_fft                | 209 ms                                                                      | 193 ms: 1.08x faster                                                |
| pyflate                    | 321 ms                                                                      | 298 ms: 1.08x faster                                                |
| scimark_monte_carlo        | 49.5 ms                                                                     | 46.1 ms: 1.08x faster                                               |
| pickle_dict                | 18.7 us                                                                     | 17.6 us: 1.06x faster                                               |
| bench_thread_pool          | 876 us                                                                      | 825 us: 1.06x faster                                                |
| mako                       | 6.96 ms                                                                     | 6.59 ms: 1.06x faster                                               |
| xml_etree_iterparse        | 67.0 ms                                                                     | 63.7 ms: 1.05x faster                                               |
| nqueens                    | 63.9 ms                                                                     | 60.9 ms: 1.05x faster                                               |
| json                       | 3.01 ms                                                                     | 2.87 ms: 1.05x faster                                               |
| unpack_sequence            | 39.2 ns                                                                     | 37.5 ns: 1.04x faster                                               |
| richards                   | 27.6 ms                                                                     | 26.6 ms: 1.04x faster                                               |
| xml_etree_generate         | 54.8 ms                                                                     | 52.8 ms: 1.04x faster                                               |
| telco                      | 4.75 ms                                                                     | 4.59 ms: 1.03x faster                                               |
| chaos                      | 44.6 ms                                                                     | 43.1 ms: 1.03x faster                                               |
| deepcopy                   | 226 us                                                                      | 219 us: 1.03x faster                                                |
| deepcopy_reduce            | 1.97 us                                                                     | 1.91 us: 1.03x faster                                               |
| typing_runtime_protocols   | 74.3 us                                                                     | 72.2 us: 1.03x faster                                               |
| create_gc_cycles           | 739 us                                                                      | 720 us: 1.03x faster                                                |
| dulwich_log                | 43.3 ms                                                                     | 42.2 ms: 1.03x faster                                               |
| xml_etree_process          | 37.1 ms                                                                     | 36.2 ms: 1.02x faster                                               |
| pprint_safe_repr           | 520 ms                                                                      | 508 ms: 1.02x faster                                                |
| pprint_pformat             | 1.07 sec                                                                    | 1.04 sec: 1.02x faster                                              |
| unpickle_pure_python       | 135 us                                                                      | 133 us: 1.02x faster                                                |
| async_tree_none            | 268 ms                                                                      | 263 ms: 1.02x faster                                                |
| crypto_pyaes               | 47.8 ms                                                                     | 46.9 ms: 1.02x faster                                               |
| logging_format             | 6.58 us                                                                     | 6.48 us: 1.02x faster                                               |
| async_tree_cpu_io_mixed    | 456 ms                                                                      | 449 ms: 1.02x faster                                                |
| xml_etree_parse            | 94.2 ms                                                                     | 92.8 ms: 1.02x faster                                               |
| chameleon                  | 4.93 ms                                                                     | 4.86 ms: 1.01x faster                                               |
| pathlib                    | 81.9 ms                                                                     | 80.7 ms: 1.01x faster                                               |
| pickle_pure_python         | 181 us                                                                      | 179 us: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                      | 464 ms: 1.01x faster                                                |
| scimark_sor                | 77.1 ms                                                                     | 76.2 ms: 1.01x faster                                               |
| logging_simple             | 6.16 us                                                                     | 6.09 us: 1.01x faster                                               |
| generators                 | 22.2 ms                                                                     | 22.0 ms: 1.01x faster                                               |
| regex_compile              | 84.4 ms                                                                     | 83.8 ms: 1.01x faster                                               |
| sqlite_synth               | 1.56 us                                                                     | 1.55 us: 1.01x faster                                               |
| scimark_lu                 | 56.5 ms                                                                     | 56.2 ms: 1.01x faster                                               |
| docutils                   | 1.59 sec                                                                    | 1.59 sec: 1.00x slower                                              |
| 2to3                       | 218 ms                                                                      | 219 ms: 1.01x slower                                                |
| json_loads                 | 13.3 us                                                                     | 13.4 us: 1.01x slower                                               |
| sympy_str                  | 167 ms                                                                      | 168 ms: 1.01x slower                                                |
| regex_dna                  | 121 ms                                                                      | 122 ms: 1.01x slower                                                |
| coverage                   | 44.9 ms                                                                     | 45.4 ms: 1.01x slower                                               |
| sympy_integrate            | 13.1 ms                                                                     | 13.3 ms: 1.01x slower                                               |
| pidigits                   | 151 ms                                                                      | 152 ms: 1.01x slower                                                |
| coroutines                 | 12.8 ms                                                                     | 12.9 ms: 1.01x slower                                               |
| dask                       | 256 ms                                                                      | 259 ms: 1.01x slower                                                |
| meteor_contest             | 75.6 ms                                                                     | 76.6 ms: 1.01x slower                                               |
| sqlglot_optimize           | 34.9 ms                                                                     | 35.4 ms: 1.01x slower                                               |
| sympy_sum                  | 86.1 ms                                                                     | 87.4 ms: 1.02x slower                                               |
| tornado_http               | 88.0 ms                                                                     | 89.4 ms: 1.02x slower                                               |
| regex_effbot               | 1.57 ms                                                                     | 1.60 ms: 1.02x slower                                               |
| gc_traversal               | 1.48 ms                                                                     | 1.51 ms: 1.02x slower                                               |
| richards_super             | 30.7 ms                                                                     | 31.4 ms: 1.02x slower                                               |
| sympy_expand               | 276 ms                                                                      | 284 ms: 1.03x slower                                                |
| regex_v8                   | 15.1 ms                                                                     | 15.5 ms: 1.03x slower                                               |
| mypy2                      | 420 ms                                                                      | 432 ms: 1.03x slower                                                |
| python_startup             | 20.3 ms                                                                     | 21.0 ms: 1.04x slower                                               |
| raytrace                   | 173 ms                                                                      | 180 ms: 1.04x slower                                                |
| python_startup_no_site     | 18.1 ms                                                                     | 19.1 ms: 1.05x slower                                               |
| bench_mp_pool              | 67.5 ms                                                                     | 71.7 ms: 1.06x slower                                               |
| async_generators           | 230 ms                                                                      | 245 ms: 1.06x slower                                                |
| hexiom                     | 4.99 ms                                                                     | 5.42 ms: 1.09x slower                                               |
| mdp                        | 1.44 sec                                                                    | 1.58 sec: 1.10x slower                                              |
| go                         | 91.2 ms                                                                     | 105 ms: 1.15x slower                                                |
| Geometric mean             | (ref)                                                                       | 1.02x faster                                                        |

Benchmark hidden because not significant (17): asyncio_tcp_ssl, async_tree_none_tg, asyncio_tcp, async_tree_memoization, sqlglot_transpile, unpickle, sqlglot_normalize, unpickle_list, async_tree_io, sqlglot_parse, json_dumps, pickle, async_tree_io_tg, deepcopy_memo, logging_silent, async_tree_memoization_tg, pycparser


# HPT report

- Reliability score: 91.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
