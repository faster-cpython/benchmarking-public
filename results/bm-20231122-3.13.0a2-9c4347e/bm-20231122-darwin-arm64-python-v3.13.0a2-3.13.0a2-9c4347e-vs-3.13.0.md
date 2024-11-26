# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.008x faster
- HPT reliability: 78.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 172 ms: 1.09x faster                                       |
| chameleon      | 5.08 ms                                                | 4.77 ms: 1.07x faster                                      |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|---------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                      | 19.8 ms                                                | 18.3 ms: 1.08x faster                                      |
| async_tree_eager                | 70.1 ms                                                | 68.3 ms: 1.03x faster                                      |
| async_tree_eager_memoization    | 168 ms                                                 | 173 ms: 1.03x slower                                       |
| async_tree_eager_tg             | 47.8 ms                                                | 49.3 ms: 1.03x slower                                      |
| async_tree_eager_memoization_tg | 138 ms                                                 | 143 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed         | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_memoization_tg       | 288 ms                                                 | 336 ms: 1.17x slower                                       |
| async_tree_none                 | 215 ms                                                 | 256 ms: 1.19x slower                                       |
| async_tree_cpu_io_mixed_tg      | 448 ms                                                 | 542 ms: 1.21x slower                                       |
| async_tree_memoization          | 268 ms                                                 | 334 ms: 1.24x slower                                       |
| async_tree_eager_io             | 514 ms                                                 | 676 ms: 1.31x slower                                       |
| async_tree_none_tg              | 198 ms                                                 | 270 ms: 1.37x slower                                       |
| async_tree_eager_io_tg          | 477 ms                                                 | 654 ms: 1.37x slower                                       |
| async_tree_io_tg                | 497 ms                                                 | 694 ms: 1.40x slower                                       |
| async_tree_io                   | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets              | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                  | (ref)                                                  | 1.17x slower                                               |

Benchmark hidden because not significant (3): async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 71.8 ms: 1.03x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| float          | 56.0 ms                                                | 56.3 ms: 1.00x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 74.6 ms: 1.05x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                      |
| regex_v8       | 17.0 ms                                                | 17.0 ms: 1.00x slower                                      |
| regex_dna      | 149 ms                                                 | 152 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 198 us: 1.08x faster                                       |
| unpickle_pure_python | 164 us                                                 | 155 us: 1.06x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 39.2 ms: 1.04x faster                                      |
| xml_etree_generate   | 57.0 ms                                                | 55.8 ms: 1.02x faster                                      |
| tomli_loads          | 1.57 sec                                               | 1.54 sec: 1.02x faster                                     |
| json_loads           | 17.0 us                                                | 16.8 us: 1.01x faster                                      |
| json_dumps           | 6.52 ms                                                | 6.57 ms: 1.01x slower                                      |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 73.6 ms                                                | 75.9 ms: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.5 ms: 1.15x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 14.7 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                      |
| mako            | 7.68 ms                                                | 7.33 ms: 1.05x faster                                      |
| genshi_xml      | 34.4 ms                                                | 33.1 ms: 1.04x faster                                      |
| django_template | 22.2 ms                                                | 21.4 ms: 1.04x faster                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                               |

All benchmarks:
===============

| Benchmark                       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|---------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles                | 1.17 ms                                                | 704 us: 1.66x faster                                       |
| typing_runtime_protocols        | 101 us                                                 | 73.5 us: 1.38x faster                                      |
| mypy2                           | 701 ms                                                 | 523 ms: 1.34x faster                                       |
| bench_mp_pool                   | 62.5 ms                                                | 48.5 ms: 1.29x faster                                      |
| gc_traversal                    | 2.91 ms                                                | 2.41 ms: 1.21x faster                                      |
| python_startup                  | 18.9 ms                                                | 16.5 ms: 1.15x faster                                      |
| generators                      | 31.5 ms                                                | 27.7 ms: 1.14x faster                                      |
| crypto_pyaes                    | 54.2 ms                                                | 48.0 ms: 1.13x faster                                      |
| go                              | 115 ms                                                 | 105 ms: 1.10x faster                                       |
| deepcopy_memo                   | 27.4 us                                                | 24.9 us: 1.10x faster                                      |
| deltablue                       | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| comprehensions                  | 12.3 us                                                | 11.2 us: 1.09x faster                                      |
| 2to3                            | 187 ms                                                 | 172 ms: 1.09x faster                                       |
| nqueens                         | 62.5 ms                                                | 57.8 ms: 1.08x faster                                      |
| pickle_pure_python              | 214 us                                                 | 198 us: 1.08x faster                                       |
| coroutines                      | 19.8 ms                                                | 18.3 ms: 1.08x faster                                      |
| scimark_monte_carlo             | 50.4 ms                                                | 46.7 ms: 1.08x faster                                      |
| genshi_text                     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                      |
| telco                           | 4.76 ms                                                | 4.42 ms: 1.08x faster                                      |
| pprint_pformat                  | 1.08 sec                                               | 1.01 sec: 1.08x faster                                     |
| pprint_safe_repr                | 533 ms                                                 | 496 ms: 1.07x faster                                       |
| deepcopy                        | 237 us                                                 | 221 us: 1.07x faster                                       |
| deepcopy_reduce                 | 2.07 us                                                | 1.93 us: 1.07x faster                                      |
| sympy_integrate                 | 11.3 ms                                                | 10.6 ms: 1.07x faster                                      |
| chameleon                       | 5.08 ms                                                | 4.77 ms: 1.07x faster                                      |
| sympy_str                       | 145 ms                                                 | 137 ms: 1.06x faster                                       |
| unpickle_pure_python            | 164 us                                                 | 155 us: 1.06x faster                                       |
| sqlglot_parse                   | 856 us                                                 | 807 us: 1.06x faster                                       |
| sympy_expand                    | 246 ms                                                 | 233 ms: 1.06x faster                                       |
| regex_compile                   | 78.6 ms                                                | 74.6 ms: 1.05x faster                                      |
| sympy_sum                       | 75.4 ms                                                | 71.6 ms: 1.05x faster                                      |
| sqlglot_normalize               | 189 ms                                                 | 180 ms: 1.05x faster                                       |
| scimark_lu                      | 76.7 ms                                                | 73.0 ms: 1.05x faster                                      |
| pyflate                         | 351 ms                                                 | 335 ms: 1.05x faster                                       |
| fannkuch                        | 284 ms                                                 | 271 ms: 1.05x faster                                       |
| sqlglot_optimize                | 34.9 ms                                                | 33.3 ms: 1.05x faster                                      |
| mako                            | 7.68 ms                                                | 7.33 ms: 1.05x faster                                      |
| xml_etree_process               | 41.0 ms                                                | 39.2 ms: 1.04x faster                                      |
| sqlglot_transpile               | 1.02 ms                                                | 983 us: 1.04x faster                                       |
| genshi_xml                      | 34.4 ms                                                | 33.1 ms: 1.04x faster                                      |
| django_template                 | 22.2 ms                                                | 21.4 ms: 1.04x faster                                      |
| bench_thread_pool               | 505 us                                                 | 487 us: 1.04x faster                                       |
| nbody                           | 74.0 ms                                                | 71.8 ms: 1.03x faster                                      |
| spectral_norm                   | 76.3 ms                                                | 74.1 ms: 1.03x faster                                      |
| regex_effbot                    | 2.63 ms                                                | 2.56 ms: 1.03x faster                                      |
| async_tree_eager                | 70.1 ms                                                | 68.3 ms: 1.03x faster                                      |
| richards                        | 35.2 ms                                                | 34.4 ms: 1.02x faster                                      |
| richards_super                  | 39.1 ms                                                | 38.3 ms: 1.02x faster                                      |
| xml_etree_generate              | 57.0 ms                                                | 55.8 ms: 1.02x faster                                      |
| tomli_loads                     | 1.57 sec                                               | 1.54 sec: 1.02x faster                                     |
| hexiom                          | 4.86 ms                                                | 4.77 ms: 1.02x faster                                      |
| pycparser                       | 705 ms                                                 | 693 ms: 1.02x faster                                       |
| logging_simple                  | 3.60 us                                                | 3.55 us: 1.02x faster                                      |
| logging_format                  | 3.89 us                                                | 3.83 us: 1.02x faster                                      |
| scimark_sor                     | 105 ms                                                 | 104 ms: 1.02x faster                                       |
| json                            | 3.03 ms                                                | 2.99 ms: 1.02x faster                                      |
| thrift                          | 466 us                                                 | 459 us: 1.02x faster                                       |
| meteor_contest                  | 74.0 ms                                                | 72.9 ms: 1.01x faster                                      |
| json_loads                      | 17.0 us                                                | 16.8 us: 1.01x faster                                      |
| raytrace                        | 181 ms                                                 | 179 ms: 1.01x faster                                       |
| pidigits                        | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| regex_v8                        | 17.0 ms                                                | 17.0 ms: 1.00x slower                                      |
| chaos                           | 41.2 ms                                                | 41.3 ms: 1.00x slower                                      |
| float                           | 56.0 ms                                                | 56.3 ms: 1.00x slower                                      |
| json_dumps                      | 6.52 ms                                                | 6.57 ms: 1.01x slower                                      |
| docutils                        | 1.44 sec                                               | 1.45 sec: 1.01x slower                                     |
| logging_silent                  | 70.1 ns                                                | 71.1 ns: 1.01x slower                                      |
| python_startup_no_site          | 14.5 ms                                                | 14.7 ms: 1.02x slower                                      |
| dulwich_log                     | 28.5 ms                                                | 29.1 ms: 1.02x slower                                      |
| regex_dna                       | 149 ms                                                 | 152 ms: 1.02x slower                                       |
| coverage                        | 46.0 ms                                                | 47.0 ms: 1.02x slower                                      |
| xml_etree_parse                 | 107 ms                                                 | 110 ms: 1.03x slower                                       |
| async_tree_eager_memoization    | 168 ms                                                 | 173 ms: 1.03x slower                                       |
| xml_etree_iterparse             | 73.6 ms                                                | 75.9 ms: 1.03x slower                                      |
| async_tree_eager_tg             | 47.8 ms                                                | 49.3 ms: 1.03x slower                                      |
| async_tree_eager_memoization_tg | 138 ms                                                 | 143 ms: 1.03x slower                                       |
| scimark_sparse_mat_mult         | 2.99 ms                                                | 3.10 ms: 1.04x slower                                      |
| mdp                             | 1.49 sec                                               | 1.56 sec: 1.05x slower                                     |
| bpe_tokeniser                   | 3.25 sec                                               | 3.40 sec: 1.05x slower                                     |
| pathlib                         | 23.4 ms                                                | 25.7 ms: 1.10x slower                                      |
| async_tree_cpu_io_mixed         | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_memoization_tg       | 288 ms                                                 | 336 ms: 1.17x slower                                       |
| async_tree_none                 | 215 ms                                                 | 256 ms: 1.19x slower                                       |
| async_tree_cpu_io_mixed_tg      | 448 ms                                                 | 542 ms: 1.21x slower                                       |
| async_tree_memoization          | 268 ms                                                 | 334 ms: 1.24x slower                                       |
| async_tree_eager_io             | 514 ms                                                 | 676 ms: 1.31x slower                                       |
| async_tree_none_tg              | 198 ms                                                 | 270 ms: 1.37x slower                                       |
| async_tree_eager_io_tg          | 477 ms                                                 | 654 ms: 1.37x slower                                       |
| async_tree_io_tg                | 497 ms                                                 | 694 ms: 1.40x slower                                       |
| async_tree_io                   | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets              | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                  | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (7): pylint, html5lib, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, scimark_fft, async_generators, tornado_http
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, dask, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 78.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.57x