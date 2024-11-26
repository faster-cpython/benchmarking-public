# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 72.4 ms: 1.01x faster                                                       |
| tornado_http   | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 790 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 807 ms: 1.03x faster                                                        |
| async_generators           | 364 ms                                                       | 359 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 78.2 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 142 ms: 1.01x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                                       |
| regex_dna      | 238 ms                                                       | 245 ms: 1.03x slower                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.4 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| json_loads           | 24.7 us                                                      | 24.6 us: 1.01x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 84.9 ms: 1.00x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 229 us: 1.06x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.63 sec: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.94 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 56.4 ms: 1.03x faster                                                       |
| django_template | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 284 us: 1.37x faster                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 1.99 ms: 1.33x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 29.3 us: 1.33x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 2.86 us: 1.22x faster                                                       |
| go                         | 167 ms                                                       | 139 ms: 1.20x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.6 ms: 1.15x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                        |
| bench_thread_pool          | 929 us                                                       | 857 us: 1.08x faster                                                        |
| thrift                     | 918 us                                                       | 851 us: 1.08x faster                                                        |
| json                       | 5.62 ms                                                      | 5.26 ms: 1.07x faster                                                       |
| fannkuch                   | 384 ms                                                       | 361 ms: 1.06x faster                                                        |
| coverage                   | 84.5 ms                                                      | 79.6 ms: 1.06x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| richards_super             | 60.2 ms                                                      | 57.0 ms: 1.06x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.34 ms: 1.05x faster                                                       |
| hexiom                     | 6.47 ms                                                      | 6.16 ms: 1.05x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                                      |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.05x faster                                                        |
| float                      | 81.6 ms                                                      | 78.2 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 790 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 802 ms: 1.04x faster                                                        |
| scimark_sor                | 125 ms                                                       | 120 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 89.1 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.94 sec: 1.03x faster                                                      |
| richards                   | 52.5 ms                                                      | 50.9 ms: 1.03x faster                                                       |
| async_tree_io              | 832 ms                                                       | 807 ms: 1.03x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 56.4 ms: 1.03x faster                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 4.69 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.4 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                       |
| pyflate                    | 493 ms                                                       | 483 ms: 1.02x faster                                                        |
| tornado_http               | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 57.9 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 359 ms: 1.01x faster                                                        |
| sympy_expand               | 506 ms                                                       | 501 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| regex_compile              | 143 ms                                                       | 142 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.7 ms: 1.01x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 72.4 ms: 1.01x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.6 us: 1.01x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 73.2 ms: 1.00x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.9 ms: 1.00x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.52 sec: 1.00x faster                                                      |
| python_startup_no_site     | 8.93 ms                                                      | 8.94 ms: 1.00x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.42 ms: 1.01x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.4 ms: 1.01x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| scimark_lu                 | 97.4 ms                                                      | 99.0 ms: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.38 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| scimark_fft                | 298 ms                                                       | 305 ms: 1.02x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 99.7 ns: 1.02x slower                                                       |
| regex_dna                  | 238 ms                                                       | 245 ms: 1.03x slower                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| chaos                      | 60.6 ms                                                      | 63.4 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 216 us                                                       | 229 us: 1.06x slower                                                        |
| raytrace                   | 267 ms                                                       | 286 ms: 1.07x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.63 sec: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (11): nbody, pickle_pure_python, sympy_str, pidigits, typing_runtime_protocols, gc_traversal, xml_etree_iterparse, logging_format, mako, asyncio_websockets, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x